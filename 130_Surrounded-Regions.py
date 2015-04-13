#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
'''

class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        region_dict = {}
        m = len(board)
        n = len(board[0])
        for i in range(m):
            region_dict[m] = []

    def getRegionsStartPoint(self, board, dic):
        for i in range(n):
            if board[0][i]=='O':
                dic[0].append(i) if i not in dic[0] else None
            if board[][i]=='O':
                dic[0].append(i) if i not in dic[0] else None



        
