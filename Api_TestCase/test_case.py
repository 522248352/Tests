# coding=utf-8

import requests
import psycopg2
import json
from public_request import Public_Request
from global_parameter import *
import random
import time
from data_base_conn import Data_Base_Conn

# 提现账户查询
def test_cash_account_enquiry():

    paths = "/transaction/showWithdrawAccount.htm"
    pam = {"partnerId": PARTNERID, "merNo": MERNO_HAVA_USERID}

    r_obj = Public_Request()
    r_resu = r_obj.public_request(pas=paths,parameters=pam)

    print(json.dumps(r_resu.json(), indent=2, sort_keys=False, ensure_ascii=False))
    assert r_resu.json()["status"] == 1
    assert r_resu.json()["code"] == 101


# 商户可用通道查询
def test_businessmen_can_use_channel():
    paths = "/channel/showMerchantChannelType.htm"
    pam = {"partnerId":PARTNERID,"merNo":MERNO_HAVA_USERID}

    r_obj = Public_Request()
    r_resu = r_obj.public_request(pas=paths,parameters=pam)

    print(json.dumps(r_resu.json(), indent=2, sort_keys=False, ensure_ascii=False))
    assert r_resu.json()["status"] == 1
    assert r_resu.json()["code"] == 11

    db = Data_Base_Conn()
    sql = "SELECT count(*) from m_channeltype_map where mer_no='171805655366242304'"
    rows = db.play(sql=sql)
    vals = rows[0][0]
    assert vals == r_resu.json()["data"]["count"]


# 添加店铺
def test_create_shop():
    paths = "/channel/addChannel.htm"
    # maths = random.choice(range(1,100))

    pam = {"partnerId":PARTNERID,
           "merNo":MERNO_HAVA_USERID,
           "channelTypeId":104073509965275136,
           "channelName":"7181ebay"+str(int(time.time())),
           "url":"http://www.baiducom",
           "email":"856@qq.com",
           "paypalEmail":"test@qq.com",
           "paypalMerInfo":11,
           "paypalAccountImageId":184836625858199552}

    r_obj = Public_Request()


    r_resu = r_obj.public_request(pas=paths,parameters=pam)

    print(json.dumps(r_resu.json(),indent=2,sort_keys=False,ensure_ascii=False))
    assert r_resu.json()["status"] == 1
    assert r_resu.json()["code"] == 20002
    mer_no = r_resu.json()["data"]["channelId"]
    # time.time()
    # print(time.localtime(time.time()))
    #
    # print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    #
    # print(type(time.time()))
    # print(int(time.time()))

    db = Data_Base_Conn()
    sql = "SELECT * from m_channel_info where channel_id = '276560765987749888'"
    rows = db.play(sql=sql)
    print(len(rows))
    for row in rows:
        print(row)

    assert len(rows) == 1


# 图片上传
def test_picture_puload():
    print("----------------------------------图片上传------------------------------------")
    paths = "/upload/image.htm"
    pam = {"partnerId": PARTNERID}
    files_png = {"image": ("278.png", open("D:\\278.png", "rb"), "image/png", {})}
    r_obj = Public_Request()
    r_resu = r_obj.public_request(pas=paths, parameters=pam, files_image=files_png)
    print(json.dumps(r_resu.json(), indent=2, sort_keys=False, ensure_ascii=False))
    assert r_resu.json()["status"] == 1
    assert r_resu.json()["code"] == 10021


# 图片上传-超过2M
def test_picture_puload_2m():
    print("----------------------------------图片上传超过2M------------------------------------")
    paths = "/upload/image.htm"
    pam = {"partnerId": PARTNERID}
    files_jpg = {"image": ("34231.jpg", open("D:\\34231.jpg", "rb"), "image/jpg", {})}
    r_obj = Public_Request()
    r_resu = r_obj.public_request(pas=paths, parameters=pam, files_image=files_jpg)
    print(json.dumps(r_resu.json(), indent=2, sort_keys=False, ensure_ascii=False))
    assert r_resu.json()["status"] == 0
    assert r_resu.json()["code"] == 10020

# ebay订单报送
def test_ebay_order_submission():

    paths = "/channelOrders/batchSendEbayOrders.htm"
    pam = {"partnerId": PARTNERID, "merNo": MERNO_HAVA_USERID, "channelTypeId": 104073509965275136, "channelId": 184836678295388160, "orders": '''[{"ebayOrderId":"TEST1-1102-001","amountPaid":"123.98","amountPaidCurrency":"USD","orderStatus":"Completed","paymentMethods":"PayPal","sellerEmail":"test@stodown.com","shippingAddress":"4699 Old Ironsides Dr Ste 150  Santa Clara CA 95054-1858 United States","shippingService":"USEconomyShippingFromGC","shippingAmount":"2","shippingCurrency":"USD","totalAmount":"23.98","totalCurrency":"USD","subtotalAmount":"21.98","subtotalCurrency":"USD","buyerUserId":"kyo857140","paidTime":"1537511875353","createdTime":"1537511875353","storageTime":"1537511875353","sellerUserId":"xin7355","extendOrderId":"238020936017!250000152520959","channelId":"184836678295388160","orderItems":[{"ebayTransactionId":"1102-001","ebayItemId":"302692199600","itemTitle":"Non-Slip Bath Rug and Bathroom Rug Carpet, 16 x 24 inches","itemSite":"US","buyerEmail":"test@aa.com","buyerFirstName":"wenjun","buyerLastName":"li","transactionPriceCurrency":"USD","transactionPriceAmount":"10.99","ebayPlatform":"eBay","transactionQuantity":"1","orderLineItemId":"302692199600-1498231110101","extendedOrderId":"238020936017!250000152520001","ebayOrderId":"TEST1-1102-001","orderId":"154467748704010912"}]}]'''}
    r_obj = Public_Request()
    r_resu = r_obj.public_request(pas=paths, parameters=pam)
    print(json.dumps(r_resu.json(), indent=2, sort_keys=False, ensure_ascii=False))
    assert r_resu.json()["status"] == 1
    assert r_resu.json()["code"] == 60000


# 余额查询
def test_yu_e_select():
    print("----------------------------- 余额查询 -----------------------------")
    paths = "/merchant/showBalance.htm"
    pam = {"partnerId": PARTNERID, "merNo": MERNO_HAVA_USERID}
    r_obj = Public_Request()
    r_resu = r_obj.public_request(pas=paths, parameters=pam)
    print(json.dumps(r_resu.json(), indent=2, sort_keys=False, ensure_ascii=False))
    assert r_resu.json()["status"] == 1
    assert r_resu.json()["code"] == 11


# 余额查询-不传MERNO
def test_yu_e_select_no_merno():
    print("----------------------------- 余额查询 -----------------------------")
    paths = "/merchant/showBalance.htm"
    pam = {"partnerId": PARTNERID}
    r_obj = Public_Request()
    r_resu = r_obj.public_request(pas=paths, parameters=pam)
    print(json.dumps(r_resu.json(), indent=2, sort_keys=False, ensure_ascii=False))
    assert r_resu.json()["status"] == 0
    assert r_resu.json()["code"] == 10041


# 开户
def test_kyc_open_accounts():

    paths = "/merchant/kyc.htm"
    nums = random.choice("python")
    pam = {"partnerId": PARTNERID,
           "accountType": 1,
           "area": "中国",
           "country": "中国",
           "province": "上海",
           "address": "上海市上海",
           "city": "上海",
           "name": "企业法人",
           "idCard": 588596854788889652,
           "idCardImg1": 241354094869118976,
           "idCardImg2": 241354094869118976,
           "merName": "api开户"+nums,
           "businessNumber": 45821,
           "business": 241354094869118976}

    r_obj = Public_Request()
    r_resu = r_obj.public_request(pas=paths,parameters=pam)
    print(json.dumps(r_resu.json(), indent=2, sort_keys=False, ensure_ascii=False))

    assert r_resu.json()["status"] == 1
    assert r_resu.json()["code"] == 10021

    db = Data_Base_Conn()
    sql_m_merchant = "SELECT * from m_merchant where mer_no='276953392935501824'"
    sql_m_audit = "SELECT * FROM m_audit WHERE MER_NO='276953392935501824'"
    rows_m_merchant = db.play(sql=sql_m_merchant)
    assert len(rows_m_merchant) == 1
    # for row in rows_m_merchant:
    #     print(row)
    rows_m_audit = db.play(sql=sql_m_audit)
    assert len(rows_m_audit) == 1


# 账户查询
def test_zhang_hu_select():
    paths = "/merchant/show.htm"
    pam = {"partnerId": PARTNERID, "merNo": MERNO_HAVA_USERID}

    r_obj = Public_Request()
    r_resu = r_obj.public_request(pas=paths, parameters=pam)
    print(json.dumps(r_resu.json(), indent=2, sort_keys=False, ensure_ascii=False))

    assert r_resu.json()["status"] == 1
    assert r_resu.json()["code"] == 101


# 账户查询-merNo不填
def test_zhang_hu_select_no_merno():

    paths = "/merchant/show.htm"
    pam = {"partnerId": PARTNERID}

    r_obj = Public_Request()
    r_resu = r_obj.public_request(pas=paths, parameters=pam)

    print(json.dumps(r_resu.json(),indent=2, sort_keys=False, ensure_ascii=False))

    assert r_resu.json()["status"] == 0
    assert r_resu.json()["code"] == 10041


# 店铺查询
def test_dian_pu_select():

    paths = "/channel/showChannel.htm"
    pam = {"partnerId": PARTNERID, "merNo": MERNO_HAVA_USERID}

    r_obj = Public_Request()
    r_resu = r_obj.public_request(pas=paths, parameters=pam)

    print(json.dumps(r_resu.json(), indent=2, sort_keys=False, ensure_ascii=False))

    db = Data_Base_Conn()
    sql = "SELECT * from m_channel_info where mer_no='171805655366242304'"

    rows = db.play(sql=sql)
    print(len(rows),r_resu.json()["data"]["count"])
    assert len(rows) == r_resu.json()["data"]["count"]


# 店铺查询-查询固定id的店铺
def test_dian_pu_select_channerid():

    paths = "/channel/showChannel.htm"
    pam = {"partnerId": PARTNERID, "merNo": MERNO_HAVA_USERID, "channelId": 274464410007928832}
    r_obj = Public_Request()
    r_resu = r_obj.public_request(pas=paths, parameters=pam)
    print(json.dumps(r_resu.json(), indent=2, sort_keys=False, ensure_ascii=False))
    assert r_resu.json()["status"] == 1
    assert r_resu.json()["code"] == 101

    db = Data_Base_Conn()
    sql = "SELECT * from m_channel_info where CHANNEL_ID='274464410007928832'"
    rows = db.play(sql=sql)
    assert len(rows) == r_resu.json()["data"]["count"] == 1


# 付款转账类型查询
def test_zhuan_zhang_type_select():

    paths = "/payment/getPaymentTypes.htm"
    pam = {"partnerId": PARTNERID,"merNo": MERNO_NO_USERID}

    r_obj = Public_Request()
    r_resu = r_obj.public_request(pas=paths, parameters=pam)

    print(json.dumps(r_resu.json(),indent=2, sort_keys=False, ensure_ascii=False))

    assert r_resu.json()["status"] == 1
    assert r_resu.json()["code"] == 11


# 付款转账汇率及手续费率查询-传金额
def test_zhuan_zhang_hui_lv_select():

    paths = "/payment/getPaymentRateOrFee.htm"
    pam = {"partnerId": PARTNERID,
            "merNo": MERNO_NO_USERID,
            "receiveCurrency": "GBP",
            "paymentCurrency": "EUR",
            "paymentAmount": 1000
           }

    r_obj = Public_Request()
    r_resu = r_obj.public_request(pas=paths, parameters=pam)
    print(json.dumps(r_resu.json(), indent=2, sort_keys=False, ensure_ascii=False))
    assert r_resu.json()["status"] == 1
    assert r_resu.json()["code"] == 11


# 付款转账汇率及手续费率查询-不传金额

def test_zhuan_zhang_hui_lv_no_amount():

    paths = "/payment/getPaymentRateOrFee.htm"
    pam = {"partnerId": PARTNERID,
           "merNo": MERNO_NO_USERID,
           "receiveCurrency": "GBP",
           "paymentCurrency": "EUR"
           }

    r_obj = Public_Request()
    r_resu = r_obj.public_request(pas=paths, parameters=pam)
    print(json.dumps(r_resu.json(), indent=2, sort_keys=False, ensure_ascii=False))

    assert r_resu.json()["status"] == 1
    assert r_resu.json()["code"] == 11


# 转账申请
def test_zhuan_zhang_apply():

    paths = "/payment/paymentApply.htm"
    pam = {"partnerId": PARTNERID,
           "merNo": MERNO_NO_USERID,
           "paymentType": 0,
           "country": "GBR",
           "apiInfo": """{"IBAN":"iban","BIC":"bic","ABA":"aba","Payee bank name":"payyname","Payee":"payee"}""",
           "receiveCurrency": "USD",
           "paymentCurrency": "EUR",
           "paymentAmount": 1000,
           "registrationNumber": 2563215500001,
           "taxDocumentImageId": 241354094869118976
    }

    r_obj = Public_Request()
    r_resu = r_obj.public_request(pas=paths, parameters=pam)

    print(json.dumps(r_resu.json(), indent=2, sort_keys=False, ensure_ascii=False))

    transactionid = r_resu.json()["data"]["transactionId"]

    print(transactionid)

    assert r_resu.json()["status"] == 1
    assert r_resu.json()["code"] == 101

    db = Data_Base_Conn()
    sql = "SELECT * FROM p_transaction where transaction_center_id =" + transactionid + "ORDER BY id desc"
    rows = db.play(sql=sql)

    assert len(rows) == 1


# 转账查询
def test_zhuan_zhang_select():

    paths = "/payment/getPaymentRecords.htm"
    pam = {"partnerId": PARTNERID, "merNo": MERNO_NO_USERID}

    r_obj = Public_Request()
    r_resu = r_obj.public_request(pas=paths, parameters=pam)

    print(json.dumps(r_resu.json(), indent=2, sort_keys=False, ensure_ascii=False))
    assert r_resu.json()["status"] == 1
    assert r_resu.json()["code"] == 11

    db = Data_Base_Conn()
    sql = "SELECT * FROM p_transaction WHERE MER_NO =" + MERNO_NO_USERID
    rows = db.play(sql=sql)
    print(type(rows))
    assert len(rows) == r_resu.json()["data"]["count"]
    for row in rows:
        print(type(row))
        print(row[0])
        print(type(row[0]))
        if str(row[0]) == str(277297765262983168):
            print(row[0])
            break


def hi(name="yasoob"):
    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    if name == "yasoob":
        return greet
    else:
        return welcome



if __name__ == '__main__':
    test_zhuan_zhang_select()

    a = hi(name='ali')
    print(a)
    print(a())
    print("费欧服成功69+01")
