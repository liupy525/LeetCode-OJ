#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''

class Solution:
    # @return a string
    def convert(self, s, nRows):
        l = [ [] for i in range(nRows) ]
        templ = []
        b = True
        t = 0
        for i in list(s):
            l[t].append(i)
            if b:
                t = (t+1) % nRows
            else:
                t = (t-1) % nRows
            if t==nRows-1:
                b = False
            if t==0:
                b = True
        for i in l:
            templ.extend(i)
        return ''.join(templ)

t = Solution()
print t.convert("PAYPALISHIRING", 3) 
