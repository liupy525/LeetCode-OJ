#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Implement pow(x, n).
'''

class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n==0:
            return 1.0
        elif n<0:
            return self.pow(1/x, -n)
        else:
            temp = self.pow(x, n/2)
            if n%2==0:
                return temp*temp
            else:
                return x*temp*temp


x = 13.54324
n = -3
t = Solution()
print t.pow(x, n)
print x**n
