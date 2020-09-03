"""
腾讯云书源。书储存在本地文件夹。
"""

from Chibrary.BookSouces.basic import BSBasic
from Chibrary import config, beans
from Chibrary.config import logger
import os
from urllib import parse
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client


class BSCos(BSBasic):
    def __init__(self):
        super().__init__()
        self.path = config.config.cos_secret.path
        self.bucket = config.config.cos_secret.bucket
        self.secret = config.config.cos_secret
        self.region = config.config.cos_secret.region
        self.client = CosS3Client(CosConfig(Region=self.region, Secret_id=self.secret.secret_id,
                                            Secret_key=self.secret.secret_key))

    def make_download_url(self, key) -> str:
        return 'https://%s.cos.%s.myqcloud.com%s/%s' % (self.bucket, self.region, self.path, key)

    """
    搜索：query为{"key": ...}结构。
    请指定page。返回list。当返回list为空的时候停止搜索。
    """

    def search(self, key, page: int = 1) -> list or None:
        # response = {}
        # while page != 0:
        #     page = page - 1
        #     response = self.client.list_objects(self.bucket,
        #                                         Delimiter="/",
        #                                         # Marker="",
        #                                         MaxKeys=1000,
        #                                         Prefix=self.path,
        #                                         EncodingType="")
        # if len(response) == 0:
        #     return None
        # result = response['Contents']
        pass
        """
        {
            'ETag': '"a5b2e1cfb08d10f6523f7e6fbf3643d5"', 
            'StorageClass': 'STANDARD', 
            'Key': 'exampleobject',
            'Owner': {
                'DisplayName': '1250000000',
                'ID': '1250000000'
            }, 
            'LastModified': '2017-08-08T09:43:35.000Z', 
            'Size': '23'
        },
        """

    """
    下载：根据key获取下载链接或者文件对象。返回None表示失败。
    key不一定是数字。
    """

    def download(self, key) -> None or beans.File:
        file = beans.File(key, url=self.make_download_url(key))
        return file

    """
    上传：根据info上传file。
    成功/失败返回True/False，不支持返回None。
    这里的file是data型。
    key被自动加上path。
    """

    def upload(self, key: str, file: beans.File) -> bool or None:
        if file.data is None:
            return False
        if not key.startswith(self.path):
            key = os.path.join(self.path, key)
        key = key.replace('\\', '/')
        self.client.put_object(
            Key=key,
            Bucket=self.bucket,
            StorageClass="STANDARD",
            EnableMD5=False,
            Body=file.data
        )
        return True

    """
    删除：根据key删除文件。
    成功/失败返回True/False，不支持返回None。
    """

    def delete(self, key) -> bool or None:
        pass
