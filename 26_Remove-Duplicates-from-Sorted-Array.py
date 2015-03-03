#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2].
'''

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A)==1:
            return 1
        if len(A)==0:
            return 0
        m, n = 1, 1
        while n<len(A):
            if A[m-1]==A[n]:
                n += 1
            else:
                A[m] = A[n]
                m += 1
                n += 1
        return m
                

        

A = [1, 1, 2]
t = Solution()
print t.removeDuplicates(A)
            
