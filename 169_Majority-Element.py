#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''

class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        s = list(set(num))
        l = [0 for i in range(len(s))]
        for i in range(len(s)):
            l[i] = num.count(s[i])
        return s[l.index(max(l))]


t = Solution()
print t.majorityElement([1,1,2,2,3,3,3])

            
