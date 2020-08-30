from pymongo import *
import time
import hashlib
from Chibrary import config
from Chibrary.config import ChibraryException, logger


class ChibraryDB:
    def __init__(self):
        self.conn = MongoClient(config.DATABASE)
        self.db = self.conn.chibrary
        self.book_init_bid()

    def clear_all(self):
        collections = ['book', 'user', 'token', 'bookSource']
        for col in collections:
            self.db[col].drop()
        self.book_init_bid()

    # 检查用户登录，返回Bool
    def user_check(self, username: str, password: str):
        password_hashed = hashlib.sha1(password.encode()).hexdigest()
        if self.user_find(username=username, password=password_hashed) is None:
            return False
        return True

    # 增加用户
    # password在前端sha1加密一次，后端再sha1加密一次
    def user_add(self, username: str, password: str):
        col = self.db.user
        password_hashed = hashlib.sha1(password.encode()).hexdigest()
        if self.user_find(username) is not None:
            raise ChibraryException.UserExists('Username %s has existed.' % username)
        level = 1
        if username in config.DEFAULT_ADMINS:
            level = 10
        col.insert_one({
            'username': username,
            'password': password_hashed,
            'info': {
                'createdAt': time.time(),
                'lastLogin': 0,
                'level': level,
            },
            'statistics': {},
        })

    # 如果指定了password的值，可以检查登录
    def user_find(self, username: str, password: str = None) -> dict or None:
        col = self.db.user
        query = {'username': username}
        if password is not None:
            query['password'] = password
        result = list(col.find(query, {'_id': 0}))
        if len(result) == 0:
            return None
        return result[0]

    # 用户名关键词搜索
    def user_search(self, keyword: str) -> list:
        col = self.db.user
        data = []
        result = list(col.find({'username': {'$regex': keyword}}, {'_id': 0}))
        data.extend(result)
        return data

    # 更新用户信息
    # 参数info中有的key才会更新
    def user_update_info(self, username: str, info: dict):
        user = self.user_find(username)
        if user is None:
            raise ChibraryException.UserNotFound('Username %s not found.' % username)
        for key in info:
            user['info'][key] = info[key]
        col = self.db.user
        col.update_one({'username': username}, {'$set': {'info': user['info']}})

    def user_update_last_login_time(self, username: str):
        user = self.user_find(username)
        if user is None:
            raise ChibraryException.UserNotFound('Username %s not found.' % username)
        user['info']['lastLogin'] = time.time()
        col = self.db.user
        col.update_one({'username': username}, {'$set': {'info': user['info']}})

    def user_delete(self, username: str):
        user = self.user_find(username)
        if user is None:
            raise ChibraryException.UserNotFound('Username %s not found.' % username)
        col = self.db.user
        col.delete_one({'username': username})

    # 创建token，格式：sha1(username + time.time() + secret)
    # 已经存在token则返回已经存在的token_data
    def token_create(self, username: str) -> dict:
        query = self.token_find_by_username(username)
        if query is not None:
            if '_id' in query:
                del query['_id']
            return query
        token = hashlib.sha1((username + str(time.time()) + config.config.secret).encode()).hexdigest()
        token_data = {
            'username': username,
            'token': token
        }
        col = self.db.token
        col.insert_one(token_data)
        return token_data

    def token_find_by_token(self, token: str) -> dict or None:
        col = self.db.token
        result = list(col.find({'token': token}, {'_id': 0}))
        if len(result) == 0:
            return None
        return result[0]

    def token_find_by_username(self, username: str) -> dict or None:
        col = self.db.token
        result = list(col.find({'username': username}, {'_id': 0}))
        if len(result) == 0:
            return None
        return result[0]

    def token_destroy(self, token: str = None, username: str = None):
        if token is None and username is None:
            logger.warning('Error. You must provide one of token and username!')
            return
        query = {}
        if token is not None:
            query['token'] = token
        if username is not None:
            query['username'] = username
        col = self.db.token
        if len(list(col.find(query))) == 0:
            return
        col.delete_one(query)

    def book_init_bid(self):
        col = self.db.book
        if len(list(col.find({'_id': 'bid'}, {'_id': 0}))) == 0:
            col.insert_one({
                '_id': 'bid',
                'sequence_value': 1,
            })

    def book_get_next_bid(self):
        col = self.db.book
        result = col.find_one_and_update({'_id': 'bid'},
                                         {'$inc': {'sequence_value': 1}})
        return result['sequence_value']

    # 返回book
    def book_add(self, name: str, author: str, description: str, info: dict = None) -> dict:
        col = self.db.book
        if self.book_find_by_name(name) is not None:
            raise ChibraryException.BookExists
        bid = self.book_get_next_bid()
        book = {
            'name': name,
            'bid': bid,
            'sources': {},
            'info': {
                'name': name,
                'bid': bid,
                'description': description,
                'author': author,
                'cover': config.DEFAULT_BOOK_COVER,
                'creartedAt': time.time(),
                'lastUpdate': 0,
                'stars': 0,
                'starCount': 0,
            }
        }
        # insert_one会自动修改源对象......
        col.insert_one(book)
        del book['_id']
        if info is not None:
            book = self.book_update_info(bid, info)
        return book

    # 返回修改后的book
    def book_update_info(self, bid: int, info: dict) -> dict:
        book = self.book_find(bid)
        if book is None:
            raise ChibraryException.BookNotFound('Book (bid=%s) not found.' % bid)
        for key in info:
            book['info'][key] = info[key]
        col = self.db.book
        col.update_one({'bid': bid}, {'$set': {'info': book['info']}})
        return book

    # 书籍源更新的时候调用
    def book_updated(self, bid: int):
        self.book_update_info(bid, {
            'lastUpdate': time.time()
        })

    def book_find(self, bid: int) -> None or dict:
        col = self.db.book
        result = list(col.find({'bid': bid}, {'_id': 0}))
        if len(result) == 0:
            return None
        return result[0]

    def book_find_by_name(self, name: str):
        col = self.db.book
        result = list(col.find({'name': name}, {'_id': 0}))
        if len(result) == 0:
            return None
        return result[0]

    # 模糊搜书：info -> name, bid, author...
    # 分页?
    def book_search(self, query: dict, page: int = 1, limit: int = 30) -> list:
        result = []
        col = self.db.book
        for key in query:
            data = list(
                col.find({'info.' + key: {'$regex': query[key]}}, {'_id': 0}).limit(limit).skip(limit * (page - 1)))
            result.extend(data)
        return result

    # 为书籍增加书源
    # source: {name, username, args:{key}}
    def book_add_source(self, bid: int, username: str, source: dict):
        book = self.book_find(bid)
        if book is None:
            raise ChibraryException.BookNotFound('Book (bid=%s) not found.' % bid)
        if 'name' not in source \
                or 'args' not in source or type(source['args']) is not dict \
                or 'key' not in source['args']:
            raise ChibraryException.ArgsError
        if self.user_find(username=username) is None:
            raise ChibraryException.UserNotFound
        col = self.db.book
        sources = book['sources']
        # 可以增加多个同类型书源
        # if source['name'] in sources:
        #     raise ChibraryException.BookSourceExists
        source['username'] = username
        source['data'] = {
            'lastUpdate': 0,
            'update': '',
        }
        if source['name'] not in sources:
            sources[source['name']] = []
        sources[source['name']].append(source)
        col.update_one({'bid': bid}, {'$set': {'sources': sources}})

    # 增加书源
    def source_add(self, name: str, author: str, description: str = '', nick: str = None):
        col = self.db.bookSource
        if self.source_find(name) is not None:
            raise ChibraryException.BookSourceExists('Book source %s exists.' % name)
        if nick is None:
            nick = name
        col.insert_one({
            'name': name,
            'info': {
                'createdAt': time.time(),
                'description': description,
                'nick': nick,
                'author': author,
            }
        })

    def source_find(self, name: str) -> dict or None:
        col = self.db.bookSource
        query = {'name': name}
        result = list(col.find(query, {'_id': 0}))
        if len(result) == 0:
            return None
        return result[0]

    # 书源关键词搜索
    def source_search(self, keyword: str) -> list:
        col = self.db.bookSource
        data = []
        result = list(col.find({'name': {'$regex': keyword}}, {'_id': 0}))
        data.extend(result)
        result = list(col.find({'info.author': {'$regex': keyword}}, {'_id': 0}))
        data.extend(result)
        result = list(col.find({'info.description': {'$regex': keyword}}, {'_id': 0}))
        data.extend(result)
        return data

    # 更新书源信息
    # 参数info中有的key才会更新
    def source_update_info(self, name: str, info: dict):
        source = self.source_find(name)
        if source is None:
            raise ChibraryException.BookSourceNotFound('Book source %s not found.' % name)
        for key in info:
            source['info'][key] = info[key]
        col = self.db.bookSource
        col.update_one({'name': name}, {'$set': {'info': source['info']}})

    def source_delete(self, name: str):
        source = self.source_find(name)
        if source is None:
            raise ChibraryException.BookSourceNotFound('Book source %s not found.' % name)
        col = self.db.bookSource
        col.delete_one({'name': name})


if __name__ == '__main__':
    ChibraryDB().clear_all()
    _db = ChibraryDB()

    '''
    # 测试token
    _data = _db.token_create('chiro')
    print(_data)
    print(_db.token_find_by_username('chiro'))
    print(_db.token_find_by_token(_data['token']))
    _db.token_destroy(username='chiro')
    print(_db.token_find_by_username('chiro'))
    '''

    '''
    # 测试user
    try:
        _db.user_delete('chiro')
    except ChibraryException.UserNotFound as e:
        print(e)
    _db.user_add('chiro', '')
    try:
        _db.user_add('chiro', '')
    except ChibraryException.UserExists as e:
        print(e)
    print(_db.user_check('chiro', ''))
    print(_db.user_find('chiro'))
    '''

    '''
    # 测试user模糊搜索
    _db.user_add('x1', '')
    _db.user_add('x2', '')
    print(_db.user_search('x'))
    '''

    '''
    # 测试bid自增
    _db.book_get_next_bid()
    _db.book_get_next_bid()
    _db.book_get_next_bid()
    print(_db.book_get_next_bid())
    '''

    '''
    # 测试book
    print(_db.book_add('MyBook', 'Chiro', '一本书。'))
    print(_db.book_find(1))
    print(_db.book_find_by_name('MyBook'))
    print(_db.book_add('MyBook2', 'Chiro', '一本书。'))
    print(_db.book_find(2))
    print(_db.book_find_by_name('MyBook2'))

    print(_db.book_search({'name': 'Book'}))

    print(_db.book_update_info(2, {
        'description': '这是修改过的描述。'
    }))

    _db.book_updated(2)
    print(_db.book_find(2))
    '''
