#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
'''

# 好神奇。。。竟然直接拼接后sort就AC了。。。
# 下面是讨论区的python实现，学习吧骚年！！！

class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        m, n = len(A), len(B)

        if m > n:
            A, B = B, A
            m, n = n, m

        imin, imax = 0, m
        while imin <= imax:
            i = (imin + imax) >> 1
            j = ((m + n + 1) >> 1) - i
            if j > 0 and i < m and B[j - 1] > A[i]:
                imin = i + 1
            elif i > 0 and j < n and A[i - 1] > B[j]:
                imax = i - 1
            else:
                if i == 0:
                    num1 = B[j - 1]
                elif j == 0:
                    num1 = A[i - 1]
                else:
                    num1 = max(A[i - 1], B[j - 1])

                if (m + n) & 1:
                    return num1

                if i == m:
                    num2 = B[j]
                elif j == n:
                    num2 = A[i]
                else:
                    num2 = min(A[i], B[j])

                return (num1 + num2) / 2.0


A = [2,3,4]
B = [1]
t = Solution()
print t.findMedianSortedArrays(A, B)

