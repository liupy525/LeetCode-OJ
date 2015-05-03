#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
'''

class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        l = list(s)
        l.reverse()
        num = 0
        for i,t in enumerate(l):
            num += (ord(t)-64) * 26**i
        return num

t = Solution()
print t.titleToNumber('AA')
