from Chibrary.BookSouces.basic import BSBasic
from Chibrary import config
from Chibrary.config import logger
import os
from urllib import parse


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

    def download(self, key) -> None or config.File:
        try:
            if key is None or len(key) == 0:
                return None
        except TypeError:
            return None
        result = self.search(key)
        if result is None or len(result) == 0:
            return None
        # with open(os.path.join(self.path, key), 'rb') as f:
        #     file = config.File(key, data=f.read())
        # return file
        file = config.File(result[0]['filename'], url='http://localhost:8001/%s' % parse.quote(result[0]['filename']))
        return file

    """
    上传：根据info上传file。
    成功/失败返回True/False，不支持返回None。
    """

    def upload(self, info: dict, file: config.File) -> bool or None:
        pass

    """
    删除：根据key删除文件。
    成功/失败返回True/False，不支持返回None。
    """

    def delete(self, key) -> bool or None:
        pass
