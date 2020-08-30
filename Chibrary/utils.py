import json
from flask import request
from Chibrary import config
from Chibrary.config import logger
from Chibrary.exceptions import *
from functools import wraps
from urllib import parse


def parse_url_query(url: str) -> dict:
    if not url.lower().startswith('http://') \
            and not url.lower().startswith('https://'):
        return {}
    query = url[url.rindex('/') + 1:]
    if '?' not in query:
        return {}
    query = query[query.index('?') + 1:]
    lines = query.split('&')
    result = {}
    for line in lines:
        if line.count('=') != 1:
            continue
        key, val = line.split('=')
        # 注意这里的类型转化处理
        if val == 'undefined':
            val = None
        else:
            try:
                val = int(val)
            except ValueError:
                try:
                    val = float(val)
                except ValueError:
                    pass
        if val is not None:
            if type(val) is str:
                result[key] = parse.unquote(val)
            else:
                result[key] = val
    return result


def form_url_query(url: str, data: dict):
    if not url.lower().startswith('http://') \
            and not url.lower().startswith('https://'):
        logger.warning('Provided wrong url %s !' % url)
        return url
    if len(data) == 0:
        return url
    query = '?'
    for key in data:
        query = query + key + '=' + parse.quote(str(data[key])) + '&'
    query = query[:-1]
    return url + query


"""
返回值格式：
{
    code: ...,
    message: ...,
    data: ...,
}
"""


def make_result(code: int, message=None, data=None):
    result = {
        'code': code,
    }
    # 根据code选message
    if message is None:
        try:
            result['message'] = config.code[str(code)]
        except ValueError:
            logger.warning('Error code %s not found!' % code)
            result['message'] = config.code['0']
    else:
        result['message'] = message
    if data is not None:
        result['data'] = data
    return result


def make_error_result(error):
    return make_result(1, message=str(error))


def dump(data):
    return json.dumps(data)


def check_args(args: dict, requirements: list):
    for r in requirements:
        if r not in args:
            return False
    return True


def format_file_size(size_by_bytes: int) -> str:
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    # 最终数值应该在1~999之间
    index = 0
    unit = units[index]
    while size_by_bytes > 1000:
        index = index + 1
        unit = units[index]
        size_by_bytes = size_by_bytes / 1000
        if index == len(units):
            break
    if size_by_bytes > 20:
        return "%.0f%s" % (size_by_bytes, unit)
    return "%.2f%s" % (size_by_bytes, unit)


def admin_check(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        args = parse_url_query(request.url)
        print(args)
        print(request)
        return f(*args, **kwargs)

    return decorated()


if __name__ == '__main__':
    print(parse_url_query('http://blog.com/sss/ssss/s?wd=dsfa&a=fdsa&a=1&b=1.1&a=s'))
    print(format_file_size(20250000))
