#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
'''

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        if len(A)==0:
            return 0
        if len(A)==1:
            return 0 if A[0]==elem else 1
        m, n = 0, 0
        while n<len(A):
            if A[n]==elem:
                n += 1
            else:
                A[m] = A[n]
                m += 1
                n += 1
        return m


t = Solution()
print t.removeElement([1,3,2,3,2,3,2,3,3,3], 3)

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        if len(A)==0:
            return 0
        if len(A)==1:
            return 0 if A[0]==elem else 1
        lo, hi = 0, len(A)-1
        while lo<=hi:
            if A[lo]==elem:
                A[lo], A[hi] = A[hi], A[lo]
                hi -= 1
            else:
                lo += 1
        return lo

t = Solution()
print t.removeElement([3,3,3], 3)
