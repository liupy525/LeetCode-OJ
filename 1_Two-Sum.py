#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''
#算法时间复杂度是O（n），这一类题的经典算法

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        d = {}
        for i in range(len(num)):
            if num[i] not in d:
                d[target-num[i]] = i
            else:
                return d[num[i]]+1, i+1

t = Solution()
#print t.twoSum([3, 2, 4], 6)
print t.twoSum([0, 4, 3, 0], 0)
