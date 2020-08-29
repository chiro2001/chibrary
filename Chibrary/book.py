import json
from flask import *
from Chibrary.server import app, db
from Chibrary.utils import *


@app.route('/user/<int:bid>', methods=['GET'])
def user_space(bid: int):
    print(request)
    return 'book %s\'s index' % bid


# 登录，返回user
@app.route('/api_v1/book/download', methods=['GET'])
def user_login():
    args = parse_url_query(request.url)
    if not check_args(args, ['username', 'password']):
        return make_result(5)  # args error
    username = args['username']
    password = args['password']
    if not db.user_check(username=username, password=password):
        return make_result(3)  # login error
    token = db.token_create(username)
    user = db.user_find(username=username)
    return make_result(0, data={
        'token': token,
        'userInfo': user
    })
