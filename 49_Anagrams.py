#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given an array of strings, return all groups of strings that are anagrams.

Note: All inputs will be in lower-case.
'''

class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        r = {}
        for i in strs:
            temp = ''.join(sorted(i))
            if temp not in r:
                r[temp] = [i]
            else:
                r[temp].append(i)
        return [ t for i in r if len(r[i])>1 for t in r[i]  ]



strs = ["tea","and","ate","eat","dan"]
t = Solution()
print t.anagrams(strs)
