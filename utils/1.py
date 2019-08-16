#coding=utf-8
import pymysql
from test_interFace.utils.config import *

def conn():

    conn = pymysql.connect(
        host='120.76.102.19',
        user='root',
        passwd='a135246A',
        db='tms')

    cursor = conn.cursor()

    # 使用execute方法执行SQL语句
    cursor.execute("SELECT * FROM add_forecastconfigurations where  ChannelCode = 'PPLPrivate';")

    # index = cursor.description
    # result = []
    # for res in cursor.fetchall():
    #     row = {}
    #     for i in range(len(index) - 1):
    #         row[index[i][0]] = res[i]
    #     result.append(row)
    # conn.close()
    # return result

    try:
        for res in cursor.fetchall():
            return res
    except Exception as err:
        raise Exception('aa')
        return err.args()
    # 使用 fetchone() 方法获取一条数据
    # data = cursor.fetchone()
    #
    # print(data,type(data))

    # return data
# 关闭数据库连接
    conn.close()

aa = conn()
print(aa)

DBNAME = Config().get('dbname')
DBHOST = Config().get('dbhost')
DBUSER = Config().get( 'dbuser')
DBPWD = Config().get('dbpassword')
DBCHARSET = Config().get('dbcharset')
DBPORT = Config().get("dbport")
print(DBHOST,DBUSER,DBPWD,DBPORT)
# conn = pymysql.connect(
#     host='120.76.102.19',
#     user='root',
#     passwd='a135246A',
#     db='tms')
#
# cursor = conn.cursor()
#
#  # 使用execute方法执行SQL语句
# cursor.execute("SELECT * FROM add_forecastconfigurations")
#
# # 使用 fetchone() 方法获取一条数据
# data = cursor.fetchone()
#
# print(data)
#
# # 关闭数据库连接
# conn.close()