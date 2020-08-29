from Chibrary.BookSouces.basic import BSBasic
from Chibrary import config
from Chibrary.config import logger
import os


class BSLocal(BSBasic):
    def __init__(self):
        super().__init__()
        self.path = './Books'
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        if os.path.isdir(self.path):
            logger.error('%s is not a dir!' % self.path)
            raise Exception('%s is not a dir!' % self.path)

    """
        搜索：query为{"bid": ..., "name": ...}结构。
        请指定page。返回list。当返回list为空的时候停止搜索。
        """

    def search(self, query: dict, page: int = 1) -> list or None:
        li = os.listdir(self.path)
        result = []
        for i in li:
            file_info = os.stat(os.path.join(self.path, i))
            if query['name'] in i:
                result.append({
                    'name': i,
                    'size': file_info.st_size,

                })

    """
    下载：根据bid获取下载链接。返回None表示失败。
    bid不一定是数字。
    """

    def download(self, bid) -> str or None:
        pass

    """
    上传：根据info上传file。
    成功/失败返回True/False，不支持返回None。
    """

    def upload(self, info: dict, file: config.File) -> bool or None:
        pass

    """
    删除：根据bid删除文件。
    成功/失败返回True/False，不支持返回None。
    """

    def delete(self, bid) -> bool or None:
        pass
