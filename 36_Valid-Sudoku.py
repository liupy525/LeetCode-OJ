#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.
'''

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        s = set()
        for i in board:
            st = ''.join(i).replace('.', '')
            se = set(st)
            if len(st)!=len(se):
                return False
        l = []
        for i in range(9):
            for j in range(len(board)):
                l.append(board[j][i])
            st = ''.join(l).replace('.', '')
            se = set(st)
            if len(se)!=len(st):
                return False
            l = []
        l = []
        for i in range(3):
            for j in range(3):
                for m in range(3):
                    for n in range(3):
                        l.append(board[i*3+m][j*3+n])
                st = ''.join(l).replace('.', '')
                se = set(st)
                if len(se)!=len(st):
                    return False
                l = []
        return True


#s = ["..4...63.",".........","5......9.","...56....","4.3.....1","...7.....","...5.....",".........","........."]
#s = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
s = ["....5..1.",".4.3.....",".....3..1","8......2.","..2.7....",".15......",".....2...",".2.9.....","..4......"]

t = Solution()
print t.isValidSudoku(s)


