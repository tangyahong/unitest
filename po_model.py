#!/usr/bin/env python
# encoding: utf-8
'''
@author: wangzai
@file: po_model.py
@time: 2020-01-15 20:23
@desc:
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Page(object):
    '''
    基础类，用于页面对象类的继承
    '''
    login_url = 'http://www.baidu.com'
