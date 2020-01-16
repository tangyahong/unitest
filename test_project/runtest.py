#!/usr/bin/env python
# encoding: utf-8
'''
@author: wangzai
@file: runtest.py
@time: 2020-01-09 18:56
@desc:
'''

'''
import unittest

#加载测试文件
from test_case import test_baidu,test_youdao

# 构造测试集

suite = unittest.TestSuite()

suite.addTest(test_baidu.MyTest("test_baidu"))
suite.addTest(test_youdao.MyTest("test_youdao"))

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite)
'''

# 利用discover()
import unittest,time
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP
import os



# =====================定义发送邮件=================================
def send_mail(file_new):
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()


    sender = '765467709@qq.com'
    receivers = 'tangyahong.gd@chinatelecom.cn'
    message = MIMEText(mail_body,'html','utf-8')
    message['From'] = Header('唐小红', 'utf-8')
    message['To'] = Header('tyh', 'utf-8')
    message['Subject'] = Header('自动化测试报告', 'utf-8')
    smtper = SMTP('smtp.qq.com')
    smtper.login(sender, 'kmyozvtmfeurbfhe')
    smtper.sendmail(sender, receivers, message.as_string())
    print('发生成功！')
    '''
    msg = MIMEText(mail_body,'html','utf-8')
    msg['Subject'] = Header("自动化测试报告",'utf-8')
    smtp = smtplib.SMTP()
    # 发送邮件服务器
    smtp.connect('smtp.qq.com')
    # 登录邮箱
    smtp.login('765467709@qq.com','zhuwoxingfu')
    # 发送邮件
    smtp.sendmail('765467709@qq.com','tangyahong.gd@chinatelecom.cn',msg.as_string())
    smtp.quit()
    print('email has send out!')
    '''

# ======查找测试报告目录，找到最近生成的测试报告文件=======
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key= lambda fn:os.path.getmtime(testreport+'\\'+fn))
    file_new = os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new


test_dir = r'F:\python\selenium-python\unitest\test_project\test_case'
test_report = r'F:\python\selenium-python\unitest\test_project\report'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == '__main__':
    # runner = unittest.TextTestRunner()
    now= time.strftime("%Y-%m-%d %H_%M_%S")
    filename = test_report+'\\'+now+'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='搜索引擎测试报告', description='用例执行情况')
    runner.run(discover)
    fp.close()

    new_report=new_report(test_report)
    send_mail(new_report)
