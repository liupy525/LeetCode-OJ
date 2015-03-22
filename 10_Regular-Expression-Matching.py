#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
'''


# 从后往前分析，判断最后一位是不是*，然后递归

class Solution:
    # @return a boolean
    cache = {}
    def isMatch(self, s, p):
        if (s,p) in self.cache:
            return self.cache[(s, p)]
        if not p:
            return not s
        if p[-1]=='*':
            if self.isMatch(s, p[:-2]):
                self.cache[(s, p)] = True
                return True
            if s and (s[-1]==p[-2] or p[-2]=='.'):
                return self.isMatch(s[:-1], p)
        else:
            if s and (p[-1]=='.' or s[-1]==p[-1]):
                return self.isMatch(s[:-1], p[:-1])

        self.cache[(s, p)] = False
        return False


