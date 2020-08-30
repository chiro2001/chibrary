import requests
import time
import json
from Chibrary.utils import *


# 普通游客场景
def test1():
    # 建立一本书
    data = json.loads(requests.get(form_url_query('http://localhost/api/v1/book/add', {
        'name': '白夜行',
        'author': '东野圭吾',
        # TODO: 限制description长度或者把请求放在其他地方。
        'description': '''《白夜行》是日本作家东野圭吾创作的长篇小说，也是其代表作。该小说于1997年1月至1999年1月间连载于期刊，单行本1999年8月在日本发行。故事围绕着一对有着不同寻常情愫的小学生展开。1973年，大阪的一栋废弃建筑内发现了一具男尸，此后19年，嫌疑人之女雪穗与被害者之子桐原亮司走上截然不同的人生道路，一个跻身上流社会，一个却在底层游走，而他们身边的人，却接二连三地离奇死去，警察经过19年的艰苦追踪，终于使真相大白。小说将无望却坚守的凄凉爱情和执著而缜密的冷静推理完美结合。2006年，小说被改编成同名电视连续剧，一举囊括第48届日剧学院赏四项大奖。'''
    })).content)
    print(data)
    # 建立一个书源(√)
    # 为书添加书源
    data = json.loads(requests.get(form_url_query('http://localhost/api/v1/book/addSource/local', {
        'bid': 1,
        'key': '东野圭吾 - 白夜行.mobi'
    })).content)
    # print(form_url_query('http://localhost/api/v1/book/addSource/local', {
    #     'bid': 1,
    #     'key': '东野圭吾 - 白夜行.mobi'
    # }))
    print(data)
    # 搜索书籍
    data = json.loads(requests.get(form_url_query('http://localhost/api/v1/book/search', {
        'name': '白'
    })).content)
    print(data)
    # 下载书籍
    data = json.loads(requests.get(form_url_query('http://localhost/api/v1/book/download/local', {
        'bid': 1,
        'key': '东野圭吾 - 白夜行.mobi'
    })).content)
    print(data)


# 用户操作场景
def test2():
    print('注册')
    print(json.loads(requests.get(form_url_query('http://localhost/api/v1/user/register', {
        'username': 'chiro',
        'password': 'test'
    })).content))
    time.sleep(2)
    print('登录')
    data = json.loads(requests.get(form_url_query('http://localhost/api/v1/user/login', {
        'username': 'chiro',
        'password': 'test'
    })).content)
    print(data)
    token = data['data']['token']['token']
    headers = {
        'Authorization': token
    }
    print('尝试注销')
    data = json.loads(requests.get('http://localhost/api/v1/user/logout', headers={}).content)
    print(data)

    print('注销')
    data = json.loads(requests.get('http://localhost/api/v1/user/logout', headers=headers).content)
    print(data)

    print('再次登录')
    data = json.loads(requests.get(form_url_query('http://localhost/api/v1/user/login', {
        'username': 'chiro',
        'password': 'test'
    })).content)
    print(data)
    token = data['data']['token']['token']
    headers = {
        'Authorization': token
    }

    time.sleep(2)
    print('修改信息')
    data = json.loads(requests.get(form_url_query('http://localhost/api/v1/user/updateInfo', {
        'head': config.DEFAULT_USER_HEAD,
        'birthday': time.time(),
        'gender': '♂'
    }), headers=headers).content)
    print(data)

    print('获取信息')
    data = json.loads(requests.get(form_url_query('http://localhost/api/v1/user/info', {
        # 'username': 'chiro',
        'head': config.DEFAULT_USER_HEAD,
        'birthday': time.time(),
        'gender': '♂'
    }), headers=headers).content)
    print(data)


# 用户上传书源场景
def test3():
    print('注册')
    print(json.loads(requests.get(form_url_query('http://localhost/api/v1/user/register', {
        'username': 'chiro',
        'password': 'test'
    })).content))
    time.sleep(2)
    print('登录')
    data = json.loads(requests.get(form_url_query('http://localhost/api/v1/user/login', {
        'username': 'chiro',
        'password': 'test'
    })).content)
    print(data)
    token = data['data']['token']['token']
    headers = {
        'Authorization': token
    }

    print('新建书籍')
    # 建立一本书
    data = json.loads(requests.get(form_url_query('http://localhost/api/v1/book/add', {
        'name': '白夜行',
        'author': '东野圭吾',
        'description': '''《白夜行》是日本作家东野圭吾创作的长篇小说，也是其代表作。'''
    }), headers=headers).content)
    print(data)
    print('为书籍增加url书源')
    data = json.loads(requests.get(form_url_query('http://localhost/api/v1/book/addSource/web', {
        'bid': 1,
        'key': 'http://localhost:8001/东野圭吾 - 白夜行.mobi'
    }), headers=headers).content)
    print(data)
    print('获取书籍信息')
    data = json.loads(requests.get(form_url_query('http://localhost/api/v1/book/1', {}), headers=headers).content)
    print(data)


if __name__ == '__main__':
    test1()
