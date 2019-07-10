# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import webbrowser
import json

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("http://www.baidu.com")
driver.set_window_size(480, 800)
driver.get("http://www.qq.com")

handle1 = driver.current_window_handle
print(handle1)

driver.find_element_by_link_text("新闻").click()
handle2 = driver.current_window_handle
print(handle2)

driver.switch_to_window(handle1)
driver.switch_to.window(handle1)
driver.find_element_by_name()







driver.find_element_by_tag_name("body").send_keys(Keys.CONTROL + '/t')
time.sleep(1)

