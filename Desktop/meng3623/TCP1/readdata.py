# coding=utf-8
##读取数据库中保存的聊天记录
import pymysql


class read_db():
    ##初始化
    def __init__(self,keyword):
        self.Keyword = keyword
        return

    def read_name(self):
        ##打开数据库连接
        self.connect = pymysql.connect(user="root", password="111111", host="localhost", database="gait", charset='utf8')
        ##创建游标
        self.cursor = self.connect.cursor()
        ##执行语句
        self.sql = "SELECT Content FROM ChatHistory WHERE Content LIKE {}".format(self.Keyword)
        self.cursor.execute(self.sql)
        self.result = self.cursor.fetchall()

        return self.result[0][0]