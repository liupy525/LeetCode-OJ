#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
'''

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        if len(num)<3:
            return []
        result = []
        num.sort()
        for i in range(len(num)-1):
            if i==0 or (i>0 and num[i]!=num[i-1]):
                expect = -num[i]
                m = i+1
                n = len(num)-1
                while m<n:
                    if num[m]+num[n]<expect:
                        m += 1
                    elif num[m]+num[n]>expect:
                        n -= 1
                    else:
                        temp = sorted([num[i], num[m], num[n]])
                        if temp not in result:
                            result.append(temp)
                        while m<n and num[m]==num[m+1]:
                            m += 1
                        while m<n and num[n]==num[n-1]:
                            n -= 1
                        m += 1
                        n -= 1
        return result
                

# num = [0, 0, 0]
# num = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
num = [7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6]
# num = [0, 0]

t = Solution()
print t.threeSum(num)


