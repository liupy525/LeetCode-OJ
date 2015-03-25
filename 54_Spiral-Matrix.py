#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
'''

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if len(matrix)==0:
            return []
        m = len(matrix)
        n = len(matrix[0])
        return self.startOrder(matrix, m , n)

    def startOrder(self, matrix, m, n):
        if m==0:
            return []
        if n==0:
            return []
        if m==1:
            return matrix[0]
        if n==1:
            return [ j for i in matrix for j in i ]
        l = []

        # step 1
        l.extend(matrix[0])
        # step2
        for i in range(1, m-1):
            l.append(matrix[i][-1])
        #step 3
        l.extend(matrix[-1][::-1])
        #step 4
        for i in range(m-2, 0, -1):
            l.append(matrix[i][0])
        #step over

        matrix2 = [ [] for i in range(m-2) ]
        for i in range(1, m-1):
            matrix2[i-1] = matrix[i][1:n-1]
        l.extend(self.startOrder(matrix2, m-2, n-2))
        return l


matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[]]
matrix = [[1,2],[3,4],[5,6],[7,8]]
matrix = [[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]
t = Solution()
print t.spiralOrder(matrix)

