#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
'''

class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        symbol = (dividend>0 and divisor>0) or (dividend<0 and divisor<0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0
        times = 1
        realdivisor = divisor
        while dividend>=divisor:
            if dividend>=realdivisor:
                dividend -= realdivisor
                result += times
                realdivisor = realdivisor << 1
                times = times << 1
            else:
                realdivisor = realdivisor >> 1
                times = times >> 1
        if not symbol:
            result = -result
        return min(max(-2147483648,result),2147483647)

t = Solution()
print t.divide(24524525242542345, 2)
print t.divide(1,1)


