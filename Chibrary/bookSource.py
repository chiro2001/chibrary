import json
from flask import *
from Chibrary.server import my_app, db
from Chibrary.utils import *


# 添加书源，只返回成功，不返回数据
@my_app.route('/api/v1/bookSource/add', methods=['GET'])
def book_source_add():
    args = parse_url_query(request.url)
    if not check_args(args, ['name', 'author']):
        return make_result(5)
    name = args['name']
    author = args['author']
    description = args.get('description', '')
    nick = args.get('nick', name)
    try:
        db.source_add(name=name, author=author, description=description, nick=nick)
    except ChibraryException.BookSourceExists:
        return make_result(7)
    return make_result(0)
