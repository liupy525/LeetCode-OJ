#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.
'''

class Solution:
    # @param {string} s
    # @return {boolean}
    def isNumber(self, s):
        s = s.strip()
        if not s:
            return False
        s = s.split('e')
        if len(s)>2:
            return False
        # things front of e
        tmp = s[0]
        if not tmp:
            return False
        if tmp[0] in ['+', '-']:
            tmp = tmp[1:]
        num_point = 0
        num_num   = 0
        for i in tmp:
            if i=='.':
                num_point += 1
            elif i>='0' and i<='9':
                num_num += 1
            else:
                return False
        if num_point>1 or num_num<1:
            return False
        # things back of e
        if len(s)==1:
            return True
        tmp = s[1]
        if not tmp:
            return False
        if tmp[0] in ['+', '-']:
            tmp = tmp[1:]
        num_num   = 0
        for i in tmp:
            if i>='0' and i<='9':
                num_num += 1
            else:
                return False
        if num_num<1:
            return False
        # test over
        return True
        
t = Solution()
print t.isNumber('9')
        
            
