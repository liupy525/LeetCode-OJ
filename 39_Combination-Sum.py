#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7, 
A solution set is: 
[7] 
[2, 2, 3] 
'''

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates.sort()
        result = []
        for i, num in enumerate(candidates):
            if num>target:
                break
            elif num==target:
                result.append([num])
            else:
                l = self.combinationSum( candidates[i:], target-num )
                if l:
                    result += [ [num]+t for t in l ]
        return result

candidates = [2,6]
target = 7
t = Solution()
print t.combinationSum( candidates, target )

