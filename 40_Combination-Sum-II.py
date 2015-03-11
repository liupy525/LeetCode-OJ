#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8, 
A solution set is: 
[1, 7] 
[1, 2, 5] 
[2, 6] 
[1, 1, 6] 
'''

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        candidates.sort()
        ans = []
        for i, num in enumerate(candidates):
            if num<target:
                l = self.combinationSum2(candidates[i+1:], target-num)
                ans += [ [num]+t for t in l if [num]+t not in ans ]
            elif num==target:
                ans.append([num]) if [num] not in ans else None
            else:
                break
        return ans


#candidates = [10,1,2,7,6,1,5]
candidates = [1,1]
target = 1
t = Solution()
print t.combinationSum2( candidates, target )

