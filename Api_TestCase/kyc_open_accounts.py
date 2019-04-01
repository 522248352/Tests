# coding=utf-8
import requests
import json
#KYC    开户-中国企业
hosts = "https://sandbox-api-onerway.ronhan.com"

url = hosts + "/merchant/kyc.htm"

#传参数据
parameter = {"partnerId":170776145556545536,
             "accountType":1,
             "area":"中国",
             "country":"中国",
             "province":"上海",
             "address":"上海市上海",
             "city":"上海",
             "name":"企业法人",
             "idCard":588596854788889652,
             "idCardImg1":241354094869118976,
             "idCardImg2":241354094869118976,
             "merName":"接口第api第一",
             "businessNumber":45821,
             "business":241354094869118976}

#响应结果数据
results = requests.post(url,parameter)

#把响应结果数据转换成Json数据打印，转成json是为了获取响应数据的内容做后面的判断
print(results.json())

#打印响应结果数据
print(results.text)

#判断返回的code，是否新增成功
if results.json()["code"] == 10021:
    print("新增success")
else:
    print("失败")
