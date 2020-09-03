import json
from io import BytesIO
import requests
import os
from Chibrary.base_logger import get_logger
from Chibrary.exceptions import *


class Config:
    class COSSecret:
        def __init__(self, secret_id: str = None, secret_key: str = None, bucket: str = None,
                     region: str = None, path: str = None):
            self.secret_id, self.secret_key = secret_id, secret_key
            self.bucket, self.region = bucket, region
            self.path = path

    def __init__(self):
        self.secret = 'default'
        self.adminPassword = 'default'
        self.cos_secret = Config.COSSecret()
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
                    self.adminPassword = self.data['adminPassword']
                except KeyError:
                    raise ChibraryException.ConfigJsonError('key:adminPassword not found')
                try:
                    secret_id, secret_key = self.data['cosSecretId'], self.data['cosSecretKey']
                    region, bucket = self.data['cosRegion'], self.data['cosBucket']
                    path = self.data['cosPath']
                    self.cos_secret = Config.COSSecret(secret_id=secret_id, secret_key=secret_key, region=region,
                                                       bucket=bucket, path=path)
                except KeyError:
                    raise ChibraryException.ConfigJsonError('key:cosSecret* not found')
        except FileNotFoundError:
            raise ChibraryException.ConfigJsonNotFound


class ResultMessage:
    class Error:
        error = 'Unknown error.'
        data = 'Invalid data.'
        login = 'Login failed.'
        args = 'Invalid args.'
        userExist = 'Username has been taken.'
        userNotFound = 'Username not found.'
        bookSourceNotFound = 'Book source not found.'
        bookSourceExist = 'Book source exist.'
        bookNotFound = 'Book not found.'
        bookExist = 'Book exist.'
        permissionNotEnough = 'You have no permission to do that.'

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
    '10': ResultMessage.Error.permissionNotEnough,
    '11': ResultMessage.Error.userNotFound,
}

"""
管理
"""

DEFAULT_ADMINS = ['chiro', ]

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
DEFAULT_USER_HEAD = 'http://bed-1254016670.cos.ap-guangzhou.myqcloud.com/my_imgs/6i8ZPn__head_fin.png'

config = Config()
logger = get_logger(__name__)

