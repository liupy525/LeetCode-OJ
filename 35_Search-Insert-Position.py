#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
'''

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        if not A:
            return 0
        if A[0]>=target:
            return 0
        if A[-1]<target:
            return len(A)
        lo, hi = 0, len(A)-1
        while lo<hi:
            mid = (lo+hi)/2
            if A[mid]<target and A[mid+1]>target:
                return mid+1
            elif A[mid]<target:
                lo = mid+1
            elif A[mid]>target:
                hi = mid
            else:
                return mid
        return lo


A = [1,2]
target = 2
t = Solution()
print t.searchInsert(A, target)

