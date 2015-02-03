#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.
'''

class Solution:
    # @return an integer
    def atoi(self, str):
        str = str.strip()
        strt = str.split(' ')
        strt = strt[0]

        try:
            t = int(strt)
        except:
            templ = [ chr(i+ord('0')) for i in range(10) ]
            templ.append('-')
            templ.append('+')
            for i in range(len(strt)):
                if strt[i] in templ:
                    continue
                else:
                    break
            try:
                t = int(strt[:i])
            except:
                t = 0
        if t >= 2**31:
            return 2**31-1
        elif t < -2**31:
            return -2**31
        else:
            return t

t = Solution()
print t.atoi('+11e530408314')
