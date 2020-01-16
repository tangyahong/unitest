#!/usr/bin/env python
# encoding: utf-8
'''
@author: wangzai
@file: test_youdao.py
@time: 2020-01-09 18:57
@desc:
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import unittest


class Youdao(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.youdao.com"


    def test_youdao(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("translateContent").clear()
        driver.find_element_by_id("translateContent").send_keys("selenium")
        driver.find_element_by_xpath("//form[@id='form']//button").click()
        time.sleep(2)
        title = driver.title
        self.assertEqual(title,"selenium_有道搜索")

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()