import json
from io import BytesIO
import os
from Chibrary.base_logger import get_logger
from Chibrary.exceptions import *


class Config:
    def __init__(self):
        self.secret = 'default'
        self.admin_password = 'default'
        try:
            # print(os.path.abspath(os.path.curdir))
            if os.path.exists('config.json'):
                file_path = 'config.json'
            else:
                file_path = 'Chibrary/config.json'
            with open(file_path, 'r') as f:
                self.data = json.load(f)
                try:
                    self.secret = self.data['secret']
                except KeyError:
                    raise ChibraryException.ConfigJsonError('key:secret not found')
                try:
                    self.admin_password = self.data['admin_password']
                except KeyError:
                    raise ChibraryException.ConfigJsonError('key:admin_password not found')
        except FileNotFoundError:
            raise ChibraryException.ConfigJsonNotFound


class ResultMessage:
    class Error:
        error = 'Unknown error.'
        data = 'Invalid data.'
        login = 'Login failed.'
        args = 'Invalid args.'
        userExist = 'Username has been taken.'
        bookSourceNotFound = 'Book source not found.'
        bookSourceExist = 'Book source exist.'
        bookNotFound = 'Book not found.'
        bookExist = 'Book exist.'

    class Success:
        success = 'Success.'


code = {
    '0': ResultMessage.Success.success,
    '1': ResultMessage.Error.error,
    '2': ResultMessage.Error.data,
    '3': ResultMessage.Error.login,
    '4': ResultMessage.Error.userExist,
    '5': ResultMessage.Error.args,
    '6': ResultMessage.Error.bookSourceNotFound,
    '7': ResultMessage.Error.bookSourceExist,
    '8': ResultMessage.Error.bookNotFound,
    '9': ResultMessage.Error.bookExist,
}

'''
常量部分
'''

# CHIBRARY_BIND = '0.0.0.0'
CHIBRARY_BIND = 'localhost'
CHIBRARY_PORT = 80
# 版本名称规范：
# 使用float方便比较大小
VERSION = 0.1
DATABASE = 'localhost'

# 默认常量
DEFAULT_BOOK_COVER_SIZE = [200, 300]
DEFAULT_BOOK_COVER = 'http://bed-1254016670.cos.ap-guangzhou.myqcloud.com/my_imgs/MR3EcJ_place_holder.png'

config = Config()
logger = get_logger(__name__)

"""
数据结构部分
"""


class File:
    def __init__(self, filename: str, data: bytes = None, url: str = None):
        if data is None and url is None:
            raise ChibraryException.FileConfigError
        self.url, self.data, self.filename = url, data, filename

    def to_dict(self):
        return {
            'filename': self.filename,
            'url': self.url
        }
