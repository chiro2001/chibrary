"""
本地书源。书储存在本地文件夹。
"""


from Chibrary.BookSouces.basic import BSBasic
from Chibrary import config, beans
from Chibrary.config import logger
import os
from urllib import parse
import traceback


class BSLocal(BSBasic):
    def __init__(self):
        super().__init__()
        self.path = './Books'
        if not os.path.exists(self.path):
            logger.warning('%s not found, mkdir.' % self.path)
            os.mkdir(self.path)
        if not os.path.isdir(self.path):
            logger.error('%s is not a dir!' % self.path)
            raise Exception('%s is not a dir!' % self.path)

    """
        搜索：query为{"key": ...}结构。
        请指定page。返回list。当返回list为空的时候停止搜索。
        """

    def search(self, key, page: int = 1) -> list or None:
        li = os.listdir(self.path)
        result = []
        for i in li:
            file_info = os.stat(os.path.join(self.path, i))
            if key in i:
                result.append({
                    'key': key,
                    'filename': i,
                    'size': file_info.st_size,
                    'cover': config.DEFAULT_BOOK_COVER,
                    'time': file_info.st_mtime
                })
                # key 是必填项
        return result

    """
    下载：根据key获取下载链接或者文件对象。返回None表示失败。
    key不一定是数字。
    """

    def download(self, key) -> None or beans.File:
        try:
            if key is None or len(key) == 0:
                return None
        except TypeError:
            return None
        result = self.search(key)
        if result is None or len(result) == 0:
            return None
        # with open(os.path.join(self.path, key), 'rb') as f:
        #     file = beans.File(key, data=f.read())
        # return file
        file = beans.File(result[0]['filename'], url='http://localhost:8001/%s' % parse.quote(result[0]['filename']))
        return file

    """
    上传：根据info上传file。
    成功/失败返回True/False，不支持返回None。
    这里的file是data形式。
    info: {key}
    """

    def upload(self, key, file: beans.File) -> bool or None:
        try:
            with open(os.path.join(self.path, key), 'wb') as f:
                f.write(file.data)
        except Exception as e:
            traceback.print_exc()
            logger.warning('Met errors: %s' % str(e))
            return False
        return True

    """
    删除：根据key删除文件。
    成功/失败返回True/False，不支持返回None。
    """

    def delete(self, key) -> bool or None:
        if not os.path.exists(os.path.join(self.path, key)):
            return False
        os.remove(os.path.join(self.path, key))
        return True
