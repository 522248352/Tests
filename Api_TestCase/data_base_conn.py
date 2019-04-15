# coding=utf-8
import json
import requests
import psycopg2
from config_py import Config_Py

# 连接数据库
class Data_Base_Conn(object):

    # 调用配置文件获取数据库连接信息
    cp = Config_Py()
    database = cp.value_get(seon="database_sandbox", opti="database")
    user = cp.value_get(seon="database_sandbox", opti="user")
    password = cp.value_get(seon="database_sandbox", opti="password")
    host = cp.value_get(seon="database_sandbox", opti="host")
    port = cp.value_get(seon="database_sandbox", opti="port")

    # 连接到一个给定的数据库
    def conn(self):
        try:
            conn = psycopg2.connect(database="test", user="ronhan", password="63oGsXpZTuOO3TEx", host="192.168.200.231", port="5432")
            # conn = psycopg2.connect(database=Data_Base_Conn.database, user=Data_Base_Conn.user, password=Data_Base_Conn.password, host=Data_Base_Conn.host, port=Data_Base_Conn.port)
            return conn
        except:
            print("数据库连接异常Error")
        else:
            print("数据库连接成功Success")

    def play(self, sql):

        # 建立游标，用来执行数据库操作
        conns = self.conn()         # 建立 连接
        course = conns.cursor()     # 根据 连接 建立游标

        try:
            # 执行SQL命令 ## 执行SQL SELECT命令
            # course.execute("""INSERT INTO k_card_type ("id", "cardtype_name", "create_time", "status") VALUES ('5', '优惠券-测试', '2019-01-29 11:12:33', '1')""")
            course.execute(sql)

            # 提交sql
            conns.commit()

            # 获取SELECT返回的 列表list，rows是列表，每一条数据是列表中的一个值，每条数据是 元组
            rows = course.fetchall()
            return rows

            # print(len(rows))
            # for row in rows:
                # print(row)  每个row是一个元组
                # print(len(row))
                # for i in row:
                #     print(i)
                # print 'id = ',row[0], 'cardtyp_name = ', row[1], 'creTime=',row[2] ,'\n'
                # print(type(row))
        except Exception as e:
            print(e+":数据库执行异常test")
        finally:
            course.close()      # 关闭游标
            conns.close()       # 关闭连接

# 关闭游标
# course.close()


# 关闭数据库连接
# conn.close()

