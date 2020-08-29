import json
from flask import *
from Chibrary.server import app, db
from Chibrary.utils import *


@app.route('/user/<string:username>', methods=['GET'])
def user_space(username: str):
    print(request)
    return 'user %s\'s space' % username


# 登录，返回user
@app.route('/api_v1/user/login', methods=['GET'])
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


@app.route('/api_v1/user/logout', methods=['GET'])
def user_logout():
    args = parse_url_query(request.url)
    if not check_args(args, ['token']):
        return make_result(5)
    db.token_destroy(token=args['token'])
    return make_result(0, data={})


# 注册，只返回成功，不返回数据
@app.route('/api_v1/user/register', methods=['GET'])
def user_register():
    args = parse_url_query(request.url)
    if not check_args(args, ['username', 'password']):
        return make_result(5)
    try:
        db.user_add(username=args['username'], password=args['password'])
    except ChibraryException.UserExists:
        return make_result(4)
    return make_result(0)
