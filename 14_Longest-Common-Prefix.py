#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Write a function to find the longest common prefix string amongst an array of strings.
'''

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        if len(strs)==1:
            return strs[0]
        prefix = ''
        i = 0
        while i<len(strs[0]) and i<len(strs[1]):
            if strs[0][i]==strs[1][i]:
                i += 1
            else:
                break
        if i!=0:
            prefix = strs[0][:i]
        if len(strs)==2:
            return prefix
        for i in range(2, len(strs)):
            if prefix==strs[i][:len(prefix)]:
                continue
            else:
                t = len(prefix)-1
                while 1:
                    if strs[i][:t]==prefix[:t]:
                        prefix = prefix[:t]
                        break
                    else:
                        t -= 1
        return prefix

t = Solution()
print t.longestCommonPrefix(['ab', 'ac'])

                
