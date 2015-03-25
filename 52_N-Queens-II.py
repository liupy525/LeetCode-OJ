#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.
'''

class Solution:
    # @return an integer
    def totalNQueens(self, n):
        Q = [ ''.join([ '.' for i in range(n) ]) for j in range(n)]
        l = [ [] for i in range(n) ]
        temp = self.method(n, Q, l, 0)
        return len(temp)


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
print t.totalNQueens(4)

