#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''

class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        return self.startGenerate(n, 1)


    def startGenerate(self, n, start):
        if n==0:
            return []
        if n==1:
            return [[start]]
        matrix = [[ 0 for i in range(n) ] for j in range(n) ]
        #step 1
        matrix[0] = [ start+i for i in range(n) ]
        start += n
        #step 2
        for i in range(n-1):
            matrix[i+1][-1] = start
            start += 1
        #step 3
        matrix[-1] = [ start-1+i for i in range(n) ][::-1]
        start += n-1
        #step 4
        for i in range(n-2,0,-1):
            matrix[i][0] = start
            start += 1
        #step over
        inner_matrix = self.startGenerate(n-2, start)
        for i in range(n-2):
            for j in range(n-2):
                matrix[i+1][j+1] = inner_matrix[i][j]
        return matrix[:]
            

n = 0
t = Solution()
r = t.generateMatrix(n)
for i in range(n):
    print r[i]

