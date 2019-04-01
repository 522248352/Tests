#coding=utf-8
import json
import requests
import psycopg2

## 连接到一个给定的数据库

#连接数据库

class Data_Base_Conn(object):

    def conn(self):
        try:
            conn = psycopg2.connect(database="test",user="ronhan",password="63oGsXpZTuOO3TEx", host="192.168.200.231", port="5432")
            return conn
        except:
            print("数据库连接异常")

    def play(self,sql):

        # 建立游标，用来执行数据库操作
        conns = self.conn()
        course = conns.cursor()

        # 执行SQL命令 ## 执行SQL SELECT命令
        # course.execute("""INSERT INTO k_card_type ("id", "cardtype_name", "create_time", "status") VALUES ('5', '优惠券-测试', '2019-01-29 11:12:33', '1')""")
        course.execute(sql)
        conns.commit()

        # 获取SELECT返回的 元组
        rows = course.fetchall()
        return rows
        # print(len(rows))
        # for row in rows:
        #     print(row)
            # print(len(row))
            # for i in row:
            #     print(i)
            # print 'id = ',row[0], 'cardtyp_name = ', row[1], 'creTime=',row[2] ,'\n'
            # print(type(row))

        course.close()
        conns.close()

# 关闭游标
# course.close()


## 关闭数据库连接
#conn.close()

