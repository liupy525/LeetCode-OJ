#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
'''

class Solution:
# @param an integer
# @return a list of string
    def generateParenthesis(self, n):
        res = {'()'}
        for i in range(n-1):
            res = { r[:m+1]+'()'+r[m+1:] for r in res for m in range(len(r)) }
        return list(res)



t = Solution()
print t.generateParenthesis(4)



class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        l = []
        for i in range(n):
            l = self.generateNextParenthesis(l)
        return l[-1]

    def generateNextParenthesis(self, l):
        if not l:
            return [['()']]
        temp = []
        num = len(l) + 1
        m = 2
        n = num-m
        pairs = []
        while m<=n and n>0:
            pairs.append((m, n))
            m += 1
            n -= 1
        for s in l[-1]:
            t = ['()'+s, s+'()', '('+s+')']
            for i in t:
                temp.append(i) if i not in temp else None
        for pair in pairs:
            for m in l[pair[0]-1]:
                for n in l[pair[1]-1]:
                    t = [m+n, n+m]
                    for i in t:
                        temp.append(i) if i not in temp else None
        l.append(temp)
        return l

t = Solution()
print t.generateParenthesis(4)
            


