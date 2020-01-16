#!/usr/bin/env python
# encoding: utf-8
'''
@author: wangzai
@file: baidu.py
@time: 2020-01-09 15:07
@desc:
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time, re
import unittest


class BaiduTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = 'http://www.baidu.com/'
        # 定义一个空数组，运行时记录错误信息记录到该数组
        self.verificationErrors = []
        # 表示是否继续接受下一个告警，初始值为True
        self.accept_next_alert = True

    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw123").clear()
        driver.find_element_by_id("kw123").send_keys("selenium ide")
        driver.find_element_by_id("su").click()

    # 判断元素是否存在
    def is_element_present(self,how,what):
        try:
            self.driver.find_element(by=how,value=what)
        except NoSuchElementException as e:
            return  False
        return True
    # 判断是否存在告警框
    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    # 获取告警框的提示信息
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

if __name__ == '__main__':
    unittest.main()
