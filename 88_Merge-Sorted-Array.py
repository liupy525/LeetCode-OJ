#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given two sorted integer arrays A and B, merge B into A as one sorted array.

Note:
You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.
'''

# 这个题很蛋疼的地方在于A的长度是预留了B的位置的（考虑C++和Java），所以我们使用的时候不能使用len（A），而应该使用m，而且，不能使用append（可能空余了什么乱七八糟的东西。。。），参看18、21、35-37行的代码。

class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        if m == 0:
            for i in range(n):
                A.insert(i, B[i])
        elif n == 0:
            None
        else:
            pointer_A = 0
            for i in range(n):
                while pointer_A < m:
                    if B[i] <= A[pointer_A]:
                        A.insert(pointer_A, B[i])
                        pointer_A += 1
                        m += 1
                        break
                    else:
                        pointer_A += 1
                if pointer_A == m:
                    A.insert(pointer_A, B[i])
                    pointer_A += 1
                    m += 1


A = [1]
B = [2]
t = Solution()
#t.merge(A, len(A), B, len(B))
t.merge(A, 1, B, 1)
print A
