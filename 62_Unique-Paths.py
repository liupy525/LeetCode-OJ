#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.
'''

# beautiful solution !!! modified by No.63 question's beautiful solution
class Solution:
# @param obstacleGrid, a list of lists of integers
# @return an integer
    def uniquePaths(self, m, n):
        ResGrid = [[0 for x in range(n+1)] for x in range(m+1)]
        ResGrid[0][1] = 1
    
        for i in range(1, m+1):
            for j in range(1, n+1):
                ResGrid[i][j] = ResGrid[i][j-1]+ResGrid[i-1][j]
    
        return ResGrid[m][n]
t = Solution()
print t.uniquePaths(3, 3)

# my own solution ....
class Solution:
    # @param m, an integer
    # @param n, an integer
    # @return an integer
    def __init__(self):
        self.l = {}
    def uniquePaths(self, m, n):
        if m>n:
            m, n = n, m
        if (m, n) in self.l:
            return self.l[(m, n)]
        if m==1:
            return 1
        if m==2:
            return n
        tmp = self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        self.l[(m, n)] = tmp
        return tmp

t = Solution()
print t.uniquePaths(3,3)


