#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
'''

class Solution:
    # @return a string
    def countAndSay(self, n):
        value = '1'
        for i in range(n-1):
            value = self.countByPre(value)
        return value

    def countByPre(self, string):
        cnt = 1
        pre = ''
        now = ''
        temp = ''
        for i in string:
            now = i
            if pre=='':
                pre = now
            elif now==pre:
                cnt += 1
            else:
                temp += str(cnt) + pre
                pre = now
                cnt = 1
        temp += str(cnt) + pre
        return temp

t = Solution()
print t.countAndSay(1)
