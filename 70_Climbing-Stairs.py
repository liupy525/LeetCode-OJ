#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

class Solution:
    # @param {integer} n
    # @return {integer}
    def __init__(self):
        self.l = {}
    def climbStairs(self, n):
        if n==1 or n==2:
            return n
        if n in self.l:
            return self.l[n]
        tmp = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.l[n] = tmp
        return tmp

n = 35
t = Solution()
print t.climbStairs(n)


