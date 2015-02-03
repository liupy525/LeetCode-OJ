#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Determine whether an integer is a palindrome. Do this without extra space.
'''

class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        x = str(x)
        y = list(x)
        y.reverse()
        y = ''.join(y)
        if x==y:
            return True
        else:
            return False

t = Solution()
print t.isPalindrome(-2147483648)

