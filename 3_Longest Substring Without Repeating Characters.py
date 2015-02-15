#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
'''

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        l = []
        lengtht = 0
        length = 0
        for i in range(len(s)):
            t = s[i]
            if t not in l:
                lengtht += 1
                l.append(t)
                if lengtht >= length:
                    length = lengtht
            else:
                if t == l[-1]:
                    l = [t]
                    lengtht = 1
                else:
                    x = l.index(t)
                    l = l[x+1:]
                    l.append(t)
                    lengtht -= x
        if lengtht >= length:
            length = lengtht
        return length

t = Solution()
print t.lengthOfLongestSubstring("pwwkew")
