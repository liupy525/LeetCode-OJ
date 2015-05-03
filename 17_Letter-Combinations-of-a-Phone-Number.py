#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

here is a picture of keyboard of telephone

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
'''

class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        if not digits:
            return 
        k = {'1':'', '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz', '0':' '}
        l = []
        for i in list(digits):
            l.append(k[i])
        temp = list(l[0])
        result = []
        for i in range(1, len(l)):
            result = []
            for m in l[i]:
                for n in temp:
                    result.append(n+m)
            temp = result[:]
        result = temp[:]
        return result

t = Solution()
print t.letterCombinations("")

                    
                


