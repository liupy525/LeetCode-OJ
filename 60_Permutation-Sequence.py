#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
'''

class Solution:
    # @return a string
    def getPermutation(self, n, k):
        k -= 1
        if k==0:
            return ''.join([ str(i+1) for i in range(n)])
        if n==1:
            return '1'
        if n==2:
            if k%2==0:
                return '12'
            if k%2==1:
                return '21'
        l = [ str(i) for i in range(1, n+1) ]
        x = [1,2,6,24,120,720,5040,40320,362880]
        for i in range(len(x)):
            if k<x[i]:
                break
        tmp = 0
        r = ''
        for j in range(n-i-1):
            r += l.pop(0)
        for j in range(i)[::-1]:
            tmp = k / x[j]
            k = k % x[j]
            r += l.pop(tmp)
        r += ''.join(l)
        return r

n = 4
k = 2
t = Solution()
print t.getPermutation(n, k)

for i in range(1,25):
    print t.getPermutation(n, i)




