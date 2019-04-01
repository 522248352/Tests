# coding=utf-8
import requests
import math
#店铺创建--Ebay
hosts = "https://sandbox-api-onerway.ronhan.com"

url = hosts + "/channel/addChannel.htm"


parameter = {"partnerId":170776145556545536,
             "merNo":171805655366242304,
             "channelTypeId":104073509965275136,
             "channelName":"7181ebay",
                 "url":"http://www.baiducom",
"email":"856@qq.com",
"paypalEmail":"test@qq.com",
"paypalMerInfo":11,
"paypalAccountImageId":184836625858199552}

r = requests.request("POST",url,params=parameter)
print(r.text)