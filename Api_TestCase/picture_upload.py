# coding=utf-8
import requests
import json

# 图片上传
hosts = "https://sandbox-api-onerway.ronhan.com"

url = hosts + "/upload/image.htm"

parameter = {"partnerId":170776145556545536}

# 图片
# rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。
files_png = {"image": ("278.png", open("D:\\278.png", "rb"), "image/png", {})}
files_jpg = {"image": ("315.jpg", open("D:\\315.jpg", "rb"), "image/jpeg", {})}

# 方法一
results = requests.post(url, data=parameter, files=files_png)
print(results.text)

# 方法二
# results = requests.request("POST",url,data=parameter,files=files_png)
# print(results.text)
open("D:\\278.png", "rb").close()