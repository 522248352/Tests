
# coding=utf-8
import requests

#商户可用通道查询
def test_businessmen_can_use_channel():
    hosts = "https://sandbox-api-onerway.ronhan.com"

    url = hosts + "/channel/showMerchantChannelType.htm"

    parameter = {"partnerId":170776145556545536,
                 "merNo":171805655366242304}

    r = requests.post(url,data=parameter)
    print(r.text)
