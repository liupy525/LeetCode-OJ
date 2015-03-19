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
        i = 0
        step = 0
        while i<len(A)-1:
            if i+A[i]>=len(A)-1:
                step += 1
                break
            maxdis = i
            nexti = i
            for j in range(i+1, i+A[i]+1):
                if j+A[j]>maxdis:
                    maxdis = j+A[j]
                    nexti = j
            i = nexti
            step += 1
        return step



#A = range(25000, 0, -1)
#A = [2,3,1,1,4]
A = [2,1]
t = Solution()
print t.jump(A)

        
