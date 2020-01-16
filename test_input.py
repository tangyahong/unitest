#!/usr/bin/env python
# encoding: utf-8
'''
@author: wangzai
@file: test_input.py
@time: 2020-01-08 20:05
@desc:
'''
import unittest


def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n % i ==0:
            return False
    return True

class Test(unittest.TestCase):
    def setUp(self):
        number = input("Enter a number:")
        self.number = int(number)

    # def test_case(self):
    #     self.assertEqual(self.number, 10, msg="your input is not 10!")

    def test_case(self):
        self.assertTrue(is_prime(self.number),msg=str(self.number)+" is not prime")
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
