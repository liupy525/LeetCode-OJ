#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''

class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        if not num:
            return []
        i = len(num)-1
        while i>0:
            if num[i-1]<num[i]:
                break
            else:
                i -= 1
        if i==0:
            return num[::-1]
        num[i:] = num[:i-1:-1]
        t = i
        while t<len(num):
            if num[i-1]<num[t]:
                break
            else:
                t += 1
        if t==len(num):
            t = i+1
        num[i-1], num[t] = num[t], num[i-1]
        return num

num = [1,2,3]

t = Solution()
for i in range(10):
    print num
    num = t.nextPermutation(num)
