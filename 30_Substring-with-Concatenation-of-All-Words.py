#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
You are given a string, S, and a list of words, L, that are all of the same length. Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.

For example, given:
S: "barfoothefoobarman"
L: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
'''

class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        L.sort()
        num = len(L)
        n = len(L[0])
        window = n*num
        findex = []
        result = []
        for i in L:
            findex.append(S.find(i))
        for i in range(min(findex), len(S)-window+1):
            findex = []
            temp = S[i:i+window]
            if temp[0:n] not in L:
                continue
            tt = [ temp[n*j:n*j+n] for j in range(num) ]
            if sorted(tt)==L:
                result.append(i)
        return result




S = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
L = ["fooo","barr","wing","ding","wing"]
t = Solution()
print t.findSubstring(S, L)
S = "barfoothefoobarman"
L = ["foo", "bar"]
t = Solution()
print t.findSubstring(S, L)
S = "a"
L = ['a']
t = Solution()
print t.findSubstring(S, L)
S = "aaa"
L = ['a', 'a']
t = Solution()
print t.findSubstring(S, L)


