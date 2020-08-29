"""
:Description: 书源的基类。
"""
from Chibrary import config


class BSBasic:
    def __init__(self):
        pass

    """
    搜索：query为{"bid": ..., "name": ...}结构。
    请指定page。返回list。当返回list为空的时候停止搜索。
    """

    def search(self, query: dict, page: int = 1) -> list or None:
        pass

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
