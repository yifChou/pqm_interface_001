# coding=utf-8

import pymysql
from utils.config import *
from utils.log import *


# 数据库操作类
# 读取配置文件
DB = "database"  # 数据库配置
dbname = Config().get('dbotsname')
dbhost = Config().get('dbotshost')
dbpassword = Config().get('dbotspassword')
dbcharset = Config().get('dbotscharset')
dbport = Config().get("dbotsport")
dbuser = Config().get("dbotsuser")


# 数据库操作类
class database:
    def __init__(self):
        #self._logger = logger
        # 这里的None相当于其它语言的NULL
        self.dbuser = dbuser
        self.dbpassword = dbpassword
        self.dbcharset = dbcharset
        self.dbport = int(dbport)
        self.dbhost = dbhost
        self.dbname = dbname
        self.conn = self.connectMySQL()

        if (self.conn):
            self.cursor = self.conn.cursor()

    # 连接
    def connectMySQL(self):
        conn = False
        try:
            conn = pymysql.connect(host=self.dbhost,
                                   user=self.dbuser,
                                   passwd=self.dbpassword,
                                   db=self.dbname,
                                   port=self.dbport,
                                   cursorclass=pymysql.cursors.DictCursor,
                                   charset=self.dbcharset
                                   )

        except Exception as err:
            logger.info("connect database failed, %s" % err)
            conn = False
        return conn

    # 查询
    def fetch_all(self, sql):
        res = ''
        if (self.conn):
            try:
                self.cursor.execute(sql)
                res = self.cursor.fetchall()
                logger.info(res)
            except Exception as err:
                res = False
                logger.info("query database exception, %s" % err)
        return res

    # 更新
    def update(self, sql):
        flag = False
        if (self.conn):
            try:
                b= self.cursor.execute(sql)
                self.conn.commit()
                print(b)
                flag = b
            except Exception as err:
                flag = 0
                logger.info("update database exception, %s" % err)

        return flag

    # 关闭连接
    def close(self):
        if (self.conn):
            try:
                if (type(self.cursor) == 'object'):
                    self.cursor.close()
                if (type(self.conn) == 'object'):
                    self.conn.close()
            except Exception as err:
                logger.info("close database exception, %s,%s,%s" % (err, type(self.cursor), type(self.conn)))

if __name__ == '__main__':
    db = database()
    for i in range(1000):
        sql = "SELECT * FROM add_forecastconfigurations where  ChannelCode = 'PPLPrivate';"
        sql2 = "SELECT status FROM ots_account_info WHERE  status='D';"
    #result = db.fetch_all(sql2)
    #rs = db.update('delete from ots_customer_info where customer_code="AUTO";')
    RS2 = db.update(sql2)
    print(RS2)