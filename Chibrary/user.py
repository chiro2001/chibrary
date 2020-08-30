import json
from flask import *
from Chibrary.server import my_app, db
from Chibrary.utils import *


@my_app.route('/user/<string:username>', methods=['GET'])
def user_space(username: str):
    print(request)
    return 'user %s\'s space' % username


# 登录，返回user
@my_app.route('/api/v1/user/login', methods=['GET'])
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
    # 更新登陆时间
    db.user_update_last_login_time(user['username'])
    return make_result(0, data={
        'token': token,
        'userInfo': user
    })


# @my_app.route('/api/v1/user/logout', methods=['GET'])
# def user_logout():
#     args = parse_url_query(request.url)
#     if not check_args(args, ['token']):
#         return make_result(5)
#     db.token_destroy(token=args['token'])
#     return make_result(0, data={})


# 注册，只返回成功，不返回数据
@my_app.route('/api/v1/user/register', methods=['GET'])
def user_register():
    args = parse_url_query(request.url)
    if not check_args(args, ['username', 'password']):
        return make_result(5)
    try:
        db.user_add(username=args['username'], password=args['password'])
    except ChibraryException.UserExists:
        return make_result(4)
    return make_result(0)


@my_app.route('/api/v1/user/logout')
@login_check
def user_logout():
    headers = dict(request.headers)
    token = headers['Authorization']
    db.token_destroy(token=token)
    return make_result(0)


# @my_app.route('/api/v1/user/check')
# @admin_check
# def user_check():
#     return ''

# 如果不指定username就用token
@my_app.route('/api/v1/user/info')
def user_info():
    args = parse_url_query(request.url)
    if not check_args(args, ['username']):
        user = get_user_from_headers()
    else:
        username = args['username']
        user = db.user_find(username=username)
    if user is None:
        return make_result(11)  # username not found
    return make_result(0, data={
        'userInfo': user
    })


@my_app.route('/api/v1/user/updateInfo')
@login_check
def user_update_info():
    user = get_user_from_headers()
    args = parse_url_query(request.url)
    if len(args) == 0:
        return make_result(5)
    if 'createdAt' in args or 'lastLogin' in args or 'status' in args:
        return make_result(5)
    if 'level' in args:
        check_admin_abort()
    if 'birthday' in args:
        if not is_number(args['birthday']):
            return make_result(5)
    for key in args:
        user['info'][key] = args[key]
    db.user_update_info(user['username'], user['info'])
    return make_result(0)
