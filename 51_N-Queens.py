#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
'''

class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        Q = [ ''.join([ '.' for i in range(n) ]) for j in range(n)]
        l = [ [] for i in range(n) ]
        return self.method(n, Q, l, 0)


    def method(self, n, Q, l, m):
        if m==n:
            return [Q[:]]
        t = [ i for i in range(n) if i not in l[m] ]
        r = []
        for i in t:
            ll = [ j[:] for j in l]
            for j in range(n):
                if i not in ll[j]:
                    ll[j].append(i)
                x = i+j-m
                y = i-j+m
                if x not in ll[j]:
                    ll[j].append(x)
                if y not in ll[j]:
                    ll[j].append(y)
            q = Q[:]
            temp = list(q[m])
            temp[i] = 'Q'
            q[m] = ''.join(temp)
            r.extend(self.method(n, q, ll, m+1))
        return r
            

t = Solution()
print t.solveNQueens(5)

