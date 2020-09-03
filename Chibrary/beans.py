"""
数据结构部分
"""
from Chibrary.exceptions import ChibraryException
from Chibrary import utils
import requests


class File:
    class DataFetchError(Exception):
        pass

    def __init__(self, filename: str, data: bytes = None, url: str = None):
        if data is None and url is None:
            raise ChibraryException.FileConfigError
        self.url, self.data, self.filename = url, data, filename

    def to_dict(self):
        return {
            'filename': self.filename,
            'url': self.url
        }

    # 用url下载数据。最好只用腾讯云链接。
    def fetch_data(self):
        if self.url is None:
            raise File.DataFetchError
        self.data = requests.get(self.url).content


# 搜索结果中的book
class BookSearched:
    def __init__(self, key, last_update: float, size_by_bytes: int):
        self.key, self.last_update, self.size_by_bytes = key, last_update, size_by_bytes
        self.size = utils.format_file_size(self.size_by_bytes)

