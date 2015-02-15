#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
'''

#最下面是牛B的方法，学习！！
#回文特点是，回文首位各减一位还是回文，所以s[i]往前看来找回文，走一遍是不会丢掉回文的

class Solution:
    # @return a string
    def longestPalindrome(self, s):
        if len(s)==1:
            return s
        l = ""
        lenl = 1
        i = 0
        lens = len(s)
        while i<lens:
            temp = s.rfind(s[i])
            if temp!=-1:
                while temp!=i:
                    if temp+1-i<=lenl:
                        break
                    elif s[i:temp+1]==s[i:temp+1][::-1]:
                        l = s[i:temp+1]
                        lenl = len(s[i:temp+1])
                        break
                    else:
                        temp = s[:temp].rfind(s[i])
            i += 1
        return l


class Solution:
    # @return a string
    def longestPalindrome(self, s):
        if len(s)==0:
            return 0
        maxLen=1
        start=0
        for i in xrange(len(s)):
            if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
                start=i-maxLen-1
                maxLen+=2
            elif i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
                start=i-maxLen
                maxLen+=1
        return s[start:start+maxLen]

t = Solution()
s = "abba"
print t.longestPalindrome(s)
#print t.testPalindrome('bb')
