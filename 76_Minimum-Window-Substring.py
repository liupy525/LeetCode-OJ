#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the emtpy string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
'''

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {string}
    def minWindow(self, s, t):
        p = [ -1 for i in range(len(t))]
        b = False
        r = {}
        for i in range(len(s)):
            tmp = t.find(s[i])
            if tmp>-1:
                p[tmp] = i
                if not b and -1 not in p:
                    b = True
                if b:
                    ma = max(p)
                    mi = min(p)
                    r[ma-mi+1] = (mi, ma)
        tmp = r[min(r)]
        return s[tmp[0]:tmp[1]+1]

s = "ADOBECODEBANC"
t = "ABC"
f = Solution()
print f.minWindow(s, t)

