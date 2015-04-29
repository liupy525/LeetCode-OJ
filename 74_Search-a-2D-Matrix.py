#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
'''

class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        if target<matrix[0][0] or target>matrix[-1][-1]:
            return False
        l = [ i[0] for i in matrix ]
        for i in range(len(l)):
            if target<l[i]:
                break
        if target>=matrix[-1][0]:
            l = matrix[-1]
        else:
            l = matrix[i-1]
        i, j = 0, len(l)-1
        while i<j:
            print i, j
            t = (i+j)/2
            if l[t]==target:
                return True
            elif l[t]>target:
                j = t
            else:
                i = t+1
        if l[i]==target or l[j]==target:
            return True
        return False

matrix = [ [1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50] ]
matrix = [ [1], [3]]
target = 3
t = Solution()
print t.searchMatrix(matrix, target)

