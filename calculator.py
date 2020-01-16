#!/usr/bin/env python
# encoding: utf-8
'''
@author: wangzai
@file: calculator.py
@time: 2020-01-08 19:33
@desc:
'''


class Count():

    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    # 加法
    def add(self):
        return self.a + self.b

    # 减法
    def sub(self):
        return self.a - self.b
