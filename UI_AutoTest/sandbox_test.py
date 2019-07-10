# coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://sandbox-manage-onerway.ronhan.com/")
driver.maximize_window()
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("123123zxc")
driver.find_element_by_xpath('//*[@id="loginForm"]/div[3]/button').click()
time.sleep(3)

driver.find_element_by_class_name("title").click()
driver.find_element_by_id("list0101").click()
time.sleep(3)

rows = driver.find_elements_by_tag_name("tr")
print(len(rows))
print(type(rows))
for row in rows:
    print(row.text)
    for a in row.find_elements_by_tag_name("td"):
        print(a.text)


driver.quit()