#coding=utf-8

import pymysql
from utils.log import *

# 打开CMS数据库连接
def connCMS():
    try:
        conn = pymysql.connect(
            host='10.168.92.105',
            user='root',
            passwd='a135246A',
            db='cms_v3')
    except Exception as e:
        return e.args

    else:
        # 使用cursor()方法获取操作游标
        cur = conn.cursor()

        # 使用execute方法执行SQL语句
        tt = cur.execute("SELECT ChannelCode FROM channelconfigurations where  ChannelCode = 'GermanyDPD'")

        # 使用 fetchone() 方法获取一条数据
        tt = cur.fetchone()

        return logger.info(tt)

    finally:

        cur.close()
        conn.close()

connCMS()
    # # 打开TMS数据库连接
    # def connTMS(self):
    #     conn = pymysql.connect(
    #         host='120.76.102.19',
    #         user='root',
    #         passwd='a135246A',
    #         db='tms')
    #
    # def selectMySql(self):
    #     conn = self.connCMS()
    #     # 使用cursor()方法获取操作游标
    #     cursor = self.conn.cursor()
    #
    #     # 使用execute方法执行SQL语句
    #     cursor.execute("SELECT * FROM channelconfigurations")
    #
    #     # 使用 fetchone() 方法获取一条数据
    #     data = cursor.fetchone()
    #
    #     print(data)
