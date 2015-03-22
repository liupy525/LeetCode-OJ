#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
'''

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        if not num:
            return []
        if len(num)==1:
            return [num] 
        if len(num)==2:
            return [num, num[::-1]]
        result = []
        for i in range(len(num)):
            temp = num[:]
            temp.pop(i)
            l = self.permute(temp)
            result.extend([ [num[i]]+t for t in l ])
        return result


num = [1,2,3,4]
t = Solution()
print t.permute(num)

