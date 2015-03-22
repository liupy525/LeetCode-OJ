#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
'''

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        if not num:
            return []
        if len(num)==1:
            return [num] 
        if len(num)==2:
            if num[0]==num[1]:
                return [num]
            else:
                return [num, num[::-1]]
        result = []
        save = []
        for i in range(len(num)):
            if num[i] in save:
                continue
            save.append(num[i])
            temp = num[:]
            temp.pop(i)
            l = self.permuteUnique(temp)
            result.extend([ [num[i]]+t for t in l ])
        return result
        

num = [1,3,1]
t = Solution()
print t.permuteUnique(num)

