#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
'''


class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        self.startSolveSudoku(board)


    def startSolveSudoku(self, board):
        #self.printSudoku(board)
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    l = self.validNum(board, i, j)
                    if not l:
                        return False
                    for t in l:
                        board[i][j] = t
                        if self.startSolveSudoku(board):
                            return True
                    board[i][j] = '.'
                    return False
        return True

    def validNum(self, board, row, col):
        row_num = board[row][:]
        col_num = [ board[i][col] for i in range(9) ]
        block_num = [ board[i][j] for i in range(row/3*3, row/3*3+3) for j in range(col/3*3, col/3*3+3)]
        temp = list(set(row_num + col_num + block_num))
        return [ j for j in [ str(i) for i in range(1, 10) ] if j not in temp ]

    def printSudoku(self, board):
        f=  open('a.txt', 'a')
        for i in board:
            for j in i:
                f.write(str(j))
                f.write(' ')
            f.write('\n')
        f.write('\n')


#board = ['53..7....', '6..195...', '.98....6.', '8...6...3', '4..8.3..1', '7...2...6', '.6....28.', '...419..5', '....8..79']
board = [[5, 3, '.', '.', 7, '.', '.', '.', '.'], [6, '.', '.', 1, 9, 5, '.', '.', '.'], ['.', 9, 8, '.', '.', '.', '.', 6, '.'], [8, '.', '.', '.', 6, '.', '.', '.', 3], [4, '.', '.', 8, '.', 3, '.', '.', 1], [7, '.', '.', '.', 2, '.', '.', '.', 6], ['.', 6, '.', '.', '.', '.', 2, 8, '.'], ['.', '.', '.', 4, 1, 9, '.', '.', 5], ['.', '.', '.', '.', 8, '.', '.', 7, 9]]
#board = [[5, 3, 2, 6, 7, 1, 4, '.', '.'], [6, '.', '.', 1, 9, 5, '.', '.', '.'], ['.', 9, 8, '.', '.', '.', '.', 6, '.'], [8, '.', '.', '.', 6, '.', '.', '.', 3], [4, '.', '.', 8, '.', 3, '.', '.', 1], [7, '.', '.', '.', 2, '.', '.', '.', 6], ['.', 6, '.', '.', '.', '.', 2, 8, '.'], ['.', '.', '.', 4, 1, 9, '.', '.', 5], ['.', '.', '.', '.', 8, '.', '.', 7, 9]]
row = 0
col = 2
t = Solution()
t.printSudoku(board)
#print t.validNum(board, row, col)
print t.solveSudoku(board)

