#!/usr/local/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        maxlist = []
        temp = 0
        temp_t = 0
        flag = 0
        if len(A)==1:
            return A[0]
        else:
            for i in range(len(A)):
                if A[i]==0:
                    maxlist.append(temp)
                    flag = 0
                    temp = 0
                elif A[i]<0:
                    maxlist.append(temp)
                    if flag==0:
                        flag = 1
                        for j in range(i+1, len(A)):
                            if temp_t==0:
                                temp_t = A[j]
                            else:
                                if A[j]==0:
                                    maxlist.append(temp_t)
                                    temp_t = 0
                                    break
                                else:
                                    temp_t *= A[j]
                            if j==len(A)-1:
                                maxlist.append(temp_t)
                                temp_t = 0
                    if temp==0:
                        temp = A[i]
                    else:
                        temp *= A[i]
                else:
                    if temp==0:
                        temp = A[i]
                    else:
                        temp *= A[i]
                if i==len(A)-1:
                    maxlist.append(temp)
            return max(maxlist)
