# coding=utf-8
import requests
from global_parameter import HOSTS

class Public_Request(object):

    def public_request(self, pas, parameters, files_image={}):
        
        url = HOSTS + pas

        r = requests.post(url=url, data=parameters, files=files_image)

        # print(r.text)
        return r


if __name__ == '__main__':
    pr = Public_Request()
    paths = "/transaction/showWithdrawAccount.htm"
    pam = {"partnerId": 170776145556545536, "merNo": 171805655366242304}
    a = pr.public_request(pas=paths, parameters=pam)
    print(type(a))
    print(type(a.json()))
    print(a.json())
    print(a.json()["data"]["list"][0])
