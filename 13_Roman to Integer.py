#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''

class Solution:
    # @return an integer
    def romanToInt(self, s):
        ge = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        shi = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        bai = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        qian = ['','M', 'MM', 'MMM']
        l = [ge, shi, bai, qian]
        result = []
        i = 0
        while s:
            temp = {0:0}
            for t in range(1, 5):
                if t>len(s):
                    break
                if s[-t:] in l[i]:
                    temp[-t] = l[i].index(s[-t:])
            result.append(str(temp[min(temp.keys())]))
            if min(temp.keys())!=0:
                s = s[:min(temp.keys())]
            i += 1
        result.reverse()
        return int(''.join(result))

t = Solution()
print t.romanToInt('MDLXX')
