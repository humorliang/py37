# -*-coding:utf-8-*-
import sqlite3
import os


class ConfigDb(object):
    '''请求配置数据库'''

    def __init__(self, dbUrl=None):
        self._dbUrl = dbUrl

    @property
    def db_url(self):
        return self._dbUrl

    @db_url.setter
    def db_url(self, path=None):
        '''设置数据库路径'''
        if path is None:
            # print(os.path.dirname(__file__))  # 获取文件目录
            # print(os.path.basename(__file__))  # 获取文件名
            # print(os.listdir(os.path.dirname(__file__)))  # 返回所有路径下的文件夹和文件名
            dir_file_list = os.listdir(os.path.dirname(__file__))  # 获取当前目录内所有文件夹和文件
            for n in dir_file_list:
                if isinstance(n, str):
                    if n.endswith('.db'):
                        self._dbUrl = os.path.join(os.path.dirname(__file__), n)
                        print(self._dbUrl)
                    else:
                        pass
                else:
                    pass
            # 没有数据库文件，则进行创建
            if self._dbUrl is None:
                with open('sqlite3.db', 'w'):
                    pass
            else:
                pass
        else:
            if not os.path.isfile(path):
                raise IOError('您输入的文件路径有误！')
            else:
                self._dbUrl = path


if __name__ == '__main__':
    con = ConfigDb()
    con.db_url = 'sqlite3.db'
    print(con.db_url)
