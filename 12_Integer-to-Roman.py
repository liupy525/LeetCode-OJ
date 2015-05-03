#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
'''

class Solution:
    # @return a string
    def intToRoman(self, num):
        ge = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        shi = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        bai = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        qian = ['','M', 'MM', 'MMM']
        l = [ge, shi, bai, qian]
        num = int(num)
        result = []
        t = num
        y = num % 10
        i = 0
        while t:
            result.append(l[i][y])
            i += 1
            t = t / 10
            y = t % 10
        result.reverse()
        return ''.join(result)

t = Solution()
print t.intToRoman('3000')
