#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
'''

class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        l = [ 0 for i in range(len(A)+1) ]
        for i,num in enumerate(A):
            if num>=0 and num<len(A)+1:
                l[num] = 1
        i = 1
        while i<len(l):
            if l[i]==0:
                break
            i += 1
        return i
            


A = [1,2]
#A = [3,4,-1,1]
#A = [4]
t = Solution()
print t.firstMissingPositive(A)
