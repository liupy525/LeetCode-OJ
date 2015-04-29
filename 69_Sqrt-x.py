#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Implement int sqrt(int x).

Compute and return the square root of x.
'''

class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        if not x:
            return 0
        low = 1
        high = x/2+1
        i = ( low + high ) / 2
        while low<high:
            if i**2==x:
                break
            if i**2<x:
                low = i + 1
            if i**2>x:
                high = i
            i = ( low+high ) / 2 
        if i**2>x:
            return i-1
        else:
            return i

t = Solution()
print t.mySqrt(3)
