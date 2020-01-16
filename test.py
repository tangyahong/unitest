#!/usr/bin/env python
# encoding: utf-8
'''
@author: wangzai
@file: test.py
@time: 2020-01-08 19:32
@desc:
'''
from calculator import Count
import unittest
from HtmlTestRunner import HTMLTestRunner


class MyTest(unittest.TestCase):
    def setUp(self):
        print("test case start")

    def tearDown(self):
        print("test case end")


class TestAdd(MyTest):

    def test_add1(self):
        j = Count(2, 3)
        self.assertEqual(j.add(), 5)

    def test_add2(self):
        j = Count(41, 76)
        self.assertEqual(j.add(), 117)


class TestSub(MyTest):

    def test_sub1(self):
        j = Count(2, 3)
        self.assertEqual(j.sub(), -1)

    def test_sub2(self):
        j = Count(30, 1)
        self.assertEqual(j.sub(), 20)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestAdd("test_add1"))
    suite.addTest(TestAdd("test_add2"))
    suite.addTest(TestSub("test_sub1"))
    suite.addTest(TestSub("test_sub2"))

    fp = open('./test.html','wb')
    runner = HTMLTestRunner(stream=fp,title='加减法测试报告',description='用例执行情况')
    # runner = unittest.TextTestRunner()
    runner.run(suite)
    fp.close()

