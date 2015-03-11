#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
'''

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        if not A:
            return -1
        lo, hi = 0, len(A)-1
        while lo<=hi:
            mid = (lo+hi)/2
            if A[mid]==target:
                return mid
            elif A[mid]<target:
                if target<A[hi]:
                    lo = mid+1
                elif target>A[hi]:
                    hi = mid-1
                else:
                    return hi
            else:
                if target>A[hi]:
                    hi = mid-1
                elif target<A[hi]:
                    lo = mid+1
                else:
                    return hi
        return -1


#A = [4,5,6,7,8,9,0,1,2,3]
A = [1, 3, 5]
target = 1
t = Solution()
print t.search(A, target)




