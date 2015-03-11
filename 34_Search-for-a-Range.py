#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        if not A:
            return [-1, -1]
        result = [-1, -1]
        lo, hi = 0, len(A)-1
        while lo<hi:
            temp = (lo+hi)/2
            if A[temp]<target:
                lo = temp+1
            else:
                hi = temp
        if A[lo]!=target:
            return [-1, -1]
        result[0] = lo
        hi = len(A)-1
        while lo<hi:
            temp = (lo+hi+1)/2
            if A[temp]>target:
                hi = temp-1
            else:
                lo = temp
        result[1] = hi
        return result

A = []
target = 8
t = Solution()
print t.searchRange(A, target)
