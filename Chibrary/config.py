import json
from Chibrary.base_logger import get_logger
from Chibrary.exceptions import *


class Config:
    def __init__(self):
        self.secret = 'default'
        try:
            with open('config.json', 'r') as f:
                self.data = json.load(f)
                try:
                    self.secret = self.data['secret']
                except KeyError:
                    raise ChibraryException.ConfigJsonError('key:secret not found')
        except FileNotFoundError:
            raise ChibraryException.ConfigJsonNotFound


class ResultMessage:
    class Error:
        error = 'Unknown error.'
        data = 'Invalid data.'
        login = 'Login failed.'
        args = 'Invalid args.'

    class Success:
        success = 'Success.'


code = {
    '0': ResultMessage.Success.success,
    '1': ResultMessage.Error.error,
    '2': ResultMessage.Error.data,
    '3': ResultMessage.Error.login,
    # '4': ResultMessage.Error.cmd,
    '5': ResultMessage.Error.args,
    # '6': ResultMessage.Error.room,
}

'''
常量部分
'''

# CHIBRARY_BIND = '0.0.0.0'
CHIBRARY_BIND = 'localhost'
CHIBRARY_PORT = 10086
# 版本名称规范：
# 使用float方便比较大小
VERSION = 0.1

# 默认常量
DEFAULT_BOOK_COVER_SIZE = [200, 300]
DEFAULT_BOOK_COVER = 'http://bed-1254016670.cos.ap-guangzhou.myqcloud.com/my_imgs/MR3EcJ_place_holder.png'

config = Config()
logger = get_logger(__name__)
