#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
'''

class Solution:
    # @param matrix, a list of lists of integers
    # @return nothing (void), do not return anything, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        row = []
        col = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row.append(i)
                    col.append(j)
        for i in row:
            matrix[i] = [ 0 for j in range(n)]
        for i in range(m):
            for j in col:
                matrix[i][j] = 0
        print matrix

matrix = [ [1,1,1], [1,0,1], [1,1,1] ]
t = Solution()
t.setZeroes(matrix)

                
