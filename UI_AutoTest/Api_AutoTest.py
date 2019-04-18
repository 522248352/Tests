# coding=utf-8
import requests
import json



hosts = "https://sandbox-api-onerway.ronhan.com"


#商户余额查询接口的url
url_1 = hosts + "/merchant/showBalance.htm"
params_1 = {"partnerId":"170776145556545536","merNo":"171805655366242304"}
r_1 = requests.post(url_1,params_1)
print("余额查询接口调用SUCCESS")
print(r_1.json())

print(r_1.url)
print(r_1.status_code)
print(r_1.headers)
print(r_1.text)
print(len(r_1.text))
js_data = json.dumps(r_1.text)
print(type(r_1))
print(type(r_1.text))
print(type(js_data))
print(type(r_1.content))

print(r_1.json())
print(type(r_1.json()))
print(r_1.json()["data"])
print(type(r_1.json()["data"]))
print(r_1.json()["data"]["balance"])
print(type(r_1.json()["data"]["balance"]))
print(r_1.json()["data"]["balance"][0])
#
#str.find(r_1.text,"status")
#print(str.find(r_1.text,"status"))

#图片上传
url_3 = hosts + "/upload/image.htm"
params_3 = {"partnerId":170776145556545536}
#files = {"file":("lol.png",open("D:/测试文件/BUG/lol.png","rb"),"image/jpeg"),}


files = {"image":("278.png",open('D:\\278.png',"rb"),"image/png",{})}
#r_3 = requests.post(url_3,params_3,headers={'Conteny-Type':'multipart/form-data'},files={"file": ("lol.png", open("D:/lol.png", "rb"), "image/jpeg", {})})

r_4 = requests.post(url_3,data=params_3,files=files)
print(r_4.text)

# r_3 = requests.request("POST",url_3,data=params_3,files=files)
# print(r_3.text)

tess_a = [{"aaa":"abc"}]
print(tess_a[0]["aaa"])
print(type(tess_a))

test_b = {"bb":[1,2,3]}
print(test_b)
print(type(test_b))