#!/usr/local/env python
# -*- coding: utf-8 -*-

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
