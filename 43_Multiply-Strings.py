#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.
'''

class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        if num1=='0' or num2=='0':
            return '0'
        return str(int(num1)*int(num2))
