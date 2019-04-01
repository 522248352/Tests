# coding=utf-8
import requests

host = "https://zentao.ronhan.com"
url = "https://sandbox-myaccount-onerway.ronhan.com/login.htm"

parms = {"username":"96521@qq.com","password":"123456asd"}

cookos = {"cookie":"agency_iuid=167871345898692608; webid=48c3bb51-6000-493c-8531-3f5fb8f1bb29; JSESSIONID=EF0A6006DC7F02C7FD6AA648AC4AAB39.onerway_web-8081"}

# rs = requests.post(url,parms)
rs = requests.request("POST",url,cookies=cookos)

print(rs.text)

