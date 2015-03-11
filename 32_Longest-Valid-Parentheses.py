#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
'''

class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        t = s.find('()')
        if t==-1:
            return 0
        num = 1
        length = []
        ss = s
        while t>-1:
            while t>0 and t+2*num-1<len(s)-1 and s[t-1]=='(' and s[t+2*num]==')':
                num += 1
                t -= 1
            if not length:
                length.append((t, t+2*num))
            else:
                length.append((length[-1][-1]+t, length[-1][-1]+t+2*num))
            s = s[t+2*num:]
            t = s.find('()')
            num = 1
        i = 0
        temp = 0
        while length!=temp:
            temp = length[:]
            i = 0
            while i<len(length)-1:
                if length[i][1]==length[i+1][0]:
                    length[i] = (length[i][0], length[i+1][1])
                    length.pop(i+1)
                else:
                    i += 1
            for i in range(len(length)):
                if length[i][0]>0 and ss[length[i][0]-1]=='(' and length[i][1]<len(ss) and ss[length[i][1]]==')':
                    length[i] = (length[i][0]-1, length[i][1]+1)
        for i in range(len(length)):
            length[i] = length[i][1]-length[i][0]
        return max(length)


t = Solution()
# )( ((((()())()()))()(())) (
s = ")(((((()())()()))()(()))("
print t.longestValidParentheses(s)
#s = '()(()))(())))'
#print t.longestValidParentheses(s)
#s = '()(()'
#print t.longestValidParentheses(s)
#s = '(()(((()'
#print t.longestValidParentheses(s)
#s = #'(()())'
#print t.longestValidParentheses(s)
