from pymongo import *


class ChibraryDB:
    DATABASE = ''

    def __init__(self):
        self.conn = MongoClient(ChibraryDB.DATABASE)
        self.db = self.conn.chibrary

    # def user_add(self, username):
