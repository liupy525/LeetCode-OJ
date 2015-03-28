#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
'''

class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        return [ int(i) for i in list(str(int(''.join([ str(i) for i in digits ]))+1)) ]


d = [1,2,3]
t = Solution()
print t.plusOne(d)

