#coding=utf-8
print("hello")

from selenium import webdriver
import time
driver = webdriver.Chrome()
from selenium.webdriver.common.keys import Keys


driver.get("https://sandbox-manage-onerway.ronhan.com/login.htm")
driver.find_element_by_id("empty0").send_keys("admin")
driver.find_element_by_id("empty1").send_keys("123123zxc")

#隐式等待5秒
driver.implicitly_wait(5)

driver.find_element_by_xpath('//*[@id="loginForm"]/div[3]/button').click()
driver.maximize_window()

time.sleep(2)

try:
    driver.find_element_by_xpath("""11//*[@id="nav-item1"]/a/span[1]""")
    print("find success")

except Exception as e:
    print("find defeat",format(e))

try:
    driver.refresh()
    print("refresh success")
except Exception as b:
    print("refresh default")

print(driver.capabilities["version"])  #浏览器版本号

driver.get("http://www.baidu.com")

cuUrl = driver.current_url

driver.find_element_by_link_text("新闻").click()

cuUrl2 = driver.current_url


def testStu (str):
    print(str)
    return

testStu(12)


