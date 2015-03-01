#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        i = -1
        while 1:
            i += 1
            t = i
            for x in range(2):
                t = -t
                for j in range(len(num)-1):
                    expect = target+t-num[j]
                    m = j+1
                    n = len(num)-1
                    while m < n:
                        if num[m]+num[n]>expect:
                            n -= 1
                        elif num[m]+num[n]<expect:
                            m += 1
                        else:
                            return num[m]+num[n]+num[j]

t = Solution()
#print t.threeSumClosest([-1,2,1,-4], 1)
print t.threeSumClosest([0, 1, 2], 3)

