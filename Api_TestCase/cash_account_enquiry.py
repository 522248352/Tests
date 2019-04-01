# coding=utf-8
import requests
import psycopg2
import json
from public_request import Public_Request
from data_base_conn import Data_Base_Conn
#提现账户查询



paths = "/transaction/showWithdrawAccount.htm"
pam = {"partnerId":170776145556545536,"merNo":171805655366242304}

request_cash = Public_Request()
r = request_cash.public_request(pas=paths,parameters=pam)
print(r.text)
print(r.url)    #返回请求url
print(r.json())     #以JSON格式解析响应内容
print(r.status_code)     #返回状态码
print(r.raise_for_status())     #如果发送了一个错误请求，如404、500等，可以通过raise_for_status()来抛出异常
print(r.encoding)       #查看requests使用了什么编码，同时可以用r.encoding属性来改变它
print(r.raw)    #获取来自服务器的原始套接字响应
print(r.headers)    #服务器返回给我们的响应头信息，也可以在传参时通过headers=XXX来定制请求头
print(r.request)         #获取原来创建的Request对象
print(r.request.headers)       #发送到服务器的请求头
assert r.json()["status"] == 1
assert r.json()["code"] == 101
print(json.dumps(r.json(), indent=2, sort_keys=False, ensure_ascii=False))
# 利用json.dumps将响应数据进行json格式的编码解析
# indent=2将输出结果缩进2个字符显示
# sort_keys=False，输出结果是否按照关键字排序
# json.dumps 序列化时对中文默认使用的ascii编码，ensure_ascii=False才会输出中文

db = Data_Base_Conn()
sql = "SELECT * FROM k_card_type"
db.play(sql=sql)
db.conn().close()




