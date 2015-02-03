#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
'''

class Solution:
    # @return a string
    def convertToTitle(self, num):
        s = []
        a = num
        while a:
            a, b = a/26, a%26
            if b != 0:
                s.append(chr(b+64))
            else:
                s.append('Z')
                a -= 1
        s.reverse()
        return ''.join(s)

t = Solution()
print t.convertToTitle(676)
