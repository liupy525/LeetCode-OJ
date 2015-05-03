#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''

class Solution:
    # @return a boolean
    def isValid(self, s):
        l = [0]
        sym = ['(', '{', '[', ')', '}', ']']
        for i in range(len(s)):
            if s[i] in sym:
                if s[i] in sym[:3]:
                    l.append(s[i])
                else:
                    if l[-1]==sym[sym.index(s[i])-3]:
                        l.pop()
                    else:
                        return False
        if len(l) != 1:
            return False
        else:
            return True

t = Solution()
print t.isValid("()")
