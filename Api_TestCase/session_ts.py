# coding=utf-8
import requests
import cookielib

# admin系统登录接口
url = "https://sandbox-manage-onerway.ronhan.com/login.htm"
headers ={"Connection": "keep-alive",
          "Content-Length": "33",
          "Cache-Control": "max-age=0",
          "Origin": "https://sandbox-manage-onerway.ronhan.com",
          "Upgrade-Insecure-Requests": "1",
          "Content-Type": "application/x-www-form-urlencoded",
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
          "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
          "Referer": "https://sandbox-manage-onerway.ronhan.com/login.htm",
          "Accept-Encoding": "gzip, deflate, br",
          "Accept-Language": "zh-CN,zh;q=0.9"
}

par = {"username":"admin","password":"123123zxc"}

seson = requests.session()  # 用session保持登录

r_resu = seson.post(url=url, headers=headers,verify=False,data=par)
print(r_resu.text)
cok = r_resu.cookies
print(cok)
print(r_resu.status_code)
print("---------------------------------------123456")


# admin系统 店铺查询请求
url1 = "https://sandbox-manage-onerway.ronhan.com/sysMerchant/queryMerchant.htm"
headers1 = {"Connection": "keep-alive",
           "Upgrade-Insecure-Requests": "1",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
           "Referer": "https://sandbox-manage-onerway.ronhan.com/index.htm",
           "Accept-Encoding": "gzip, deflate, br",
           "Accept-Language": "zh-CN,zh;q=0.9"

}

r_resu1 = seson.request(method="GET", url=url1, headers=headers1, verify=False)
print(r_resu1.text)


# url = "https://www.baidu.com/"
# r = requests.get(url, verify=False)
#
# #将RequestsCookieJar转换成字典
# c = requests.utils.dict_from_cookiejar(r.cookies)
#
# print(r.cookies)
# print(type(r.cookies))
#
# print(c)
# print(type(c))
#
#
# for a in r.cookies:
#     print(a.value)