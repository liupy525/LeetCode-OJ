#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
'''

class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        if A[0]>=len(A)-1:
            return 1
        step = [0]
        for i,num in enumerate(A[-2::-1]):
            tstep = 50000
            for t in range(i-num+1, i+1):
                if t<=0:
                    tstep = 1
                elif step[t]:
                    tstep = min(tstep, step[t]+1)
            step.append(tstep)
        return step[-1]



A = range(25000, 0, -1)
t = Solution()
print t.jump(A)

        
