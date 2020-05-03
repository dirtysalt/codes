#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
print(driver.title)
elem = driver.find_element_by_xpath('//*[@id="kw"]')
elem.send_keys("test selenium")
elem.send_keys(Keys.RETURN)
print(driver.title)
driver.close()

