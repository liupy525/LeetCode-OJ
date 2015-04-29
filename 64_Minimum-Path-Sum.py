#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''

class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    continue
                if i==0:
                    grid[i][j] += grid[i][j-1]
                    continue
                if j==0:
                    grid[i][j] += grid[i-1][j]
                    continue
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]

grid = [ [1,2,1], [2,1,2], [3,1,1] ]
grid = [ [1,2,1] ]
grid = [ [1] ]
t = Solution()
print t.minPathSum(grid)


