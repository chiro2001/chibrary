import threading
import time
import os
from Chibrary import server
import tester


def start_tester():
    # 在local的books设置一个文件服务器
    base_dir = os.path.abspath('.')
    os.chdir('./Chibrary/BookSouces/Books')
    os.system('start python -m http.server 8001')
    os.chdir(base_dir)
    time.sleep(0.3)
    tester.test1()


if __name__ == '__main__':
    th = threading.Thread(target=start_tester)
    th.setDaemon(True)
    th.start()

    server.db.clear_all()
    server.launch()
