import json
import os
from flask import *
from Chibrary.server import my_app, db
from Chibrary.utils import *
import Chibrary.BookSouces as Sources


@my_app.route('/book/<int:bid>', methods=['GET'])
def book_index(bid: int):
    print(request)
    return 'book %s\'s index' % bid


@my_app.route('/api/v1/book/updateInfo')
@login_check
def book_update_info():
    args = parse_url_query(request.url)
    if 'bid' not in args:
        return make_result(5)
    bid = args['bid']
    if not is_number(bid):
        return
    book = db.book_find()
    if 'stars' in args or 'bid' in args or 'createdAt' in args or 'lastUpdate' in args or 'starCount' in args:
        return make_result(5)
    for key in args:
        book['info'][key] = args[key]
    db.book_update_info(book['bid'], book['info'])
    return make_result(0)


# 添加书籍，返回数据
@my_app.route('/api/v1/book/add', methods=['GET'])
def book_add():
    args = parse_url_query(request.url)
    if not check_args(args, ['name', 'author', 'description']):
        return make_result(5)
    try:
        result = db.book_add(args['name'], args['author'], args['description'])
    except ChibraryException.BookExists:
        return make_result(9)
    return make_result(0, data={
        'bookInfo': result
    })


# 添加书籍，返回数据
@my_app.route('/api/v1/book/<int:bid>', methods=['GET'])
def book_info(bid: int):
    try:
        book = db.book_find(bid)
    except ChibraryException.BookNotFound:
        return make_result(8)
    return make_result(0, data={
        'bookInfo': book
    })


# 按照数据的书源搜索书籍
@my_app.route('/api/v1/book/search', methods=['GET'])
def book_search():
    args = parse_url_query(request.url)
    # page参数可选
    if len(args) == 0:
        return make_result(5)  # args error
    page = args.get('page', 1)
    if 'page' in args:
        del args['page']
    result = db.book_search(args, page=page)
    return make_result(0, data={
        'searchResult': {
            'data': result,
            'page': page
        }
    })


# 参数是书源，返回download数据结构
# 返回值中的filename有时候是缺省的
@my_app.route('/api/v1/book/download/<string:source_name>', methods=['GET'])
def book_download(source_name: str):
    args = parse_url_query(request.url)
    if not check_args(args, ['bid', 'key']):
        return make_result(5)  # args error
    # bid还有要用来统计下载量什么的
    bid = args['bid']
    key = args['key']
    try:
        source = db.source_find(source_name)
    except ChibraryException.BookSourceNotFound:
        return make_result(6)  # book source
    source_instance = Sources.utils.sources[source['name']]()
    file = source_instance.download(key)
    if file is None:
        return make_result(8)
    if file.url is not None:
        return make_result(0, data={
            'download': file.to_dict()
        })
    # TODO: 直接返回文件内容的书源应该先内网上传之后再返回下载地址
    return make_result(0, data={
        'download': {
            'url': config.DEFAULT_BOOK_COVER,
            'filename': os.path.basename(config.DEFAULT_BOOK_COVER)
        }
    })


# # 直接返回下载链接重定向或者404
# @my_app.route('/api/v1/download/<int:bid>/<string:name>')
# def book_download_directly(bid: int, name: str):
#     book = db.book_find(bid)
#     if book is None:
#         abort(404)
#     if name not in book['sources']:
#         abort(404)
#


# 为书籍添加书源，只返回成功，不返回数据
@my_app.route('/api/v1/book/addSource/<string:name>', methods=['GET'])
@login_check
def book_add_source(name: str):
    args = parse_url_query(request.url)
    if not check_args(args, ['bid', 'key']):
        return make_result(5)
    if db.source_find(name) is None:
        return make_result(8)  # book source not found
    bid = args['bid']
    key = args['key']
    source = {
        'name': name,
        'args': {
            'key': key
        }
    }
    user = get_user_from_headers()
    username = user['username']
    try:
        db.book_add_source(bid, username, source=source)
    except ChibraryException.BookNotFound:
        return make_result(8)
    except ChibraryException.BookSourceExists:
        return make_result(7)
    return make_result(0)
