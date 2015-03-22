#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
'''

class Solution:
    # @param matrix, a list of lists of integers
    # @return nothing (void), do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(0, n/2):
            for j in range(n-1-2*i):
                matrix[i][i+j], matrix[i+j][n-1-i] = matrix[i+j][n-1-i], matrix[i][i+j]
                matrix[i][i+j], matrix[n-1-i][n-1-i-j] = matrix[n-1-i][n-1-i-j], matrix[i][i+j]
                matrix[i][i+j], matrix[n-1-i-j][i] = matrix[n-1-i-j][i], matrix[i][i+j]
    def printmatrix(self, matrix):
        for i in matrix:
            for j in i:
                if j<10:
                    print str(j)+' ',
                else:
                    print j,
            print 
        print 


matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
t = Solution()
print t.rotate(matrix)
