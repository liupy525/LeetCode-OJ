#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
'''

class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        temp = [len(A)-1]
        for i in range(len(A)-2, -1, -1):
            if i+A[i]>=temp[-1]:
                temp.append(i)
        if temp[-1]==0:
            return True
        else:
            return False


A = [2,3,1,1,4]
A = [3,2,1,0,4]
A = [2,5,0,0]
t = Solution()
print t.canJump(A)

        
