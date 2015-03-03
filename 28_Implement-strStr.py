#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''

class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        if not haystack and not needle:
            return 0
        for i in range(len(haystack)):
            j = 0
            for j in range(len(needle)):
                if i+j==len(haystack):
                    return -1
                if haystack[i+j]!=needle[j]:
                    j = -1
                    break
            if j!=-1:
                return i
        return -1


t = Solution()
#print t.strStr('abcdeftfde', 'bc')
#print t.strStr("mississippi", "a")
print t.strStr('','asdf')


class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        l = self.preparePi(needle)
        pT = 0
        pS = 0
        while pT<len(haystack)-len(needle)+1:
            if pS==0 and haystack[pT]!=needle[0]:
                pT += 1
                continue
            while pS<len(needle):
                if haystack[pT+pS]==needle[pS]:
                    pS += 1
                else:
                    pT += pS-l[pS-1]
                    pS = l[pS-1]
                    break
            if pS==len(needle):
                return pT
        return -1

    def preparePi(self, s):
        p = 0
        l = [0]
        for i in range(1, len(s)):
            if s[i]==s[p]:
                p += 1
                l.append(p)
            else:
                p = 0
                l.append(p)
        return l




        
t = Solution()
#print t.strStr('abcdeftfde', 'bc')
print t.strStr("mississippi", "pi")
#print t.strStr('','asdf')
#print t.strStr('aaa', 'aaaa')
