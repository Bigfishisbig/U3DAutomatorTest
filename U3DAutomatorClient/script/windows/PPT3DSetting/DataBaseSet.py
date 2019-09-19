#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql
import traceback
from main.object.enum import *
import os

class DataBase:
    def __init__(self):
        flag = os.getenv(Environment.DataFlag)
        self.flag = flag
        self.config = {
            'host': '192.168.239.135',
            'port': 3306,
            'user': "root",
            'passwd': "123",
            'db': "edu_project",
            'charset': 'utf8',
        }
        # self.db = pymysql.connect(host="192.168.239.135",
        #                      port=3306,
        #                      user="root",
        #                      passwd="123",
        #                      db="edu_project",
        #                      charset='utf8')

    def databaseOperate(self, sql):
        if self.flag == "N":
            return [0 for x in range(0, 20)]

        # 打开数据库连接
        db = pymysql.connect(**self.config)
        # #print "sql1:", sql
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        try:
            # 使用execute方法执行SQL语句
            cursor.execute(sql)

            # 提交到数据库执行
            db.commit()

            # 使用 fetchone() 方法获取一条数据
            # data = cursor.fetchone()

            # #print "Database version : %s " % data

        except:
            # 发生错误时回滚

            db.rollback()
            traceback.print_exc()
        # 关闭数据库连接
        db.close()

    def getData(self, sql):
        if self.flag == "N":
            return [0 for x in range(0, 20)]

        db = pymysql.connect(**self.config)
        # #print "sql2:", sql
        cursor = db.cursor()
        data = None
        try:
            cursor.execute(sql)
            db.commit()
            data = cursor.fetchone()
            #print data
        except:
            db.rollback()
            traceback.print_exc()
        # 关闭数据库连接
        db.close()
        return data