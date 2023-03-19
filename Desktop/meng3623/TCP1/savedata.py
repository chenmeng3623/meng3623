# coding=utf-8
##保存聊天记录到数据库

import pymysql
import re

##写入数据到数据库
class write_db():
    ##初始化
    def __init__(self,information):
        ##创建连接
        self.db = pymysql.connect(user="root",password="111111",host="localhost",database="wechat",charset='utf8')
        ##建立游标
        self.cursor = self.db.cursor()
        ##创建表名
        self.table_name = 'ChatHistory'
        self.c = information

    ##判断表是否存在。不存在新建；存在插入数据
    def table_exists(self):
        # 查看数据库中的所有表
        sql = 'show tables'
        self.cursor.execute(sql)
        tables = [self.cursor.fetchall()]
        tables_list = re.findall('(\'.*?\')',str(tables))
        tables_list = [re.sub("'",'',each) for each in tables_list]
        #判断'ChatHistory表'是否存在
        #不存在创建表
        if self.table_name not in tables_list:
            sql = "CREATE TABLE ChatHistory (Index INT(1000), Content VARCHAR(1024))"
            self.cursor.execute(sql)
            self.db.commit()
            self.cursor.close()
            self.db.close()

        #存在填写聊天记录
        else:
            sql = "INSERT INTO ChatHistory (Index,ChatContent) VALUES ('{}','{}')"
            newsql = sql.format(self.c[0])  ##将聊天信息填入

            self.cursor.execute(newsql)
            self.db.commit()
            self.cursor.close()
            self.db.close()




