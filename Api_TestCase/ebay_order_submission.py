# coding=utf-8
import requests
import json

#ebay订单报送

hosts = "https://sandbox-api-onerway.ronhan.com"

url = hosts + "/channelOrders/batchSendEbayOrders.htm"

parameter = {"partnerId":170776145556545536,"merNo":171805655366242304,"channelTypeId":104073509965275136,"channelId":184836678295388160,"orders":'''[{"ebayOrderId":"TEST1-1102-001","amountPaid":"123.98","amountPaidCurrency":"USD","orderStatus":"Completed","paymentMethods":"PayPal","sellerEmail":"test@stodown.com","shippingAddress":"4699 Old Ironsides Dr Ste 150  Santa Clara CA 95054-1858 United States","shippingService":"USEconomyShippingFromGC","shippingAmount":"2","shippingCurrency":"USD","totalAmount":"23.98","totalCurrency":"USD","subtotalAmount":"21.98","subtotalCurrency":"USD","buyerUserId":"kyo857140","paidTime":"1537511875353","createdTime":"1537511875353","storageTime":"1537511875353","sellerUserId":"xin7355","extendOrderId":"238020936017!250000152520959","channelId":"184836678295388160","orderItems":[{"ebayTransactionId":"1102-001","ebayItemId":"302692199600","itemTitle":"Non-Slip Bath Rug and Bathroom Rug Carpet, 16 x 24 inches","itemSite":"US","buyerEmail":"test@aa.com","buyerFirstName":"wenjun","buyerLastName":"li","transactionPriceCurrency":"USD","transactionPriceAmount":"10.99","ebayPlatform":"eBay","transactionQuantity":"1","orderLineItemId":"302692199600-1498231110101","extendedOrderId":"238020936017!250000152520001","ebayOrderId":"TEST1-1102-001","orderId":"154467748704010912"}]}]'''}
print(parameter["partnerId"])
jsonsss = json.dumps(parameter)
# heads = {"Content-Type":"text/html"}
results = requests.post(url,data=parameter)
print(parameter["orders"])
print(results.text)


