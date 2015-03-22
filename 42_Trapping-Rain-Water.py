#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
'''

class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        if len(A)<3:
            return 0
        water = 0
        start = 0
        end = 1
        l = []
        record = end
        while start<=len(A)-3:
            if A[start]>0 and A[start+1]<A[start]:
                while A[end]<A[start]:
                    if A[end]>=A[record]:
                        record = end
                    l.append(A[start]-A[end])
                    if end<len(A)-1:
                        end += 1
                    else:
                        break
                if end==len(A)-1 and A[end]<= A[record]:
                    l = [ l[i]-A[start]+A[record] for i in range(len(l)-end+record) ]
                    water += sum(l)
                    start = record
                    end = record+1
                    record = end
                    l = []
                else:
                    water += sum(l)
                    start = end
                    end = start+1
                    record = end
                    l = []
            else:
                start += 1
                end = start+1
        return water


A = [0,1,0,2,1,0,1,3,2,1,2,1]
#A = [0,1,0,2,1,0,1,3,2,1,0,0]
A = [2,0,2]
#A = [1,0,1]
#A = [4,2,3]
#A = [i-1 for i in A]
#A = [i-1 for i in A]
t = Solution()
print t.trap(A)
