#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.
'''

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        current = 0
        result = A[0]
        for i in A:
            current += i
            result = max(result, current)
            current = max(0, current)
        return result




A = [-2,1,-3,4,-1,2,1,-5,4,]
t = Solution()
print t.maxSubArray(A)

