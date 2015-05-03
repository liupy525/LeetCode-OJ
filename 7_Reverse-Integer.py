#!/usr/local/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return an integer
    def reverse(self, x):
        y = list(str(x))
        y.reverse()
        if y[-1]=='-':
            y.pop()
            return int('-' + ''.join(y))
        else:
            return int(''.join(y))
