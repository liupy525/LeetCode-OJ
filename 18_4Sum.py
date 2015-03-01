#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
'''

#class Solution:
#    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
#    def fourSum(self, num, target):
#        if len(num)==4:
#            return [sorted(num)] if sum(num)==target else []
#        result = []
#        num.sort()
#        for i in range(len(num)-2):
#            for j in range(i+1,len(num)-1):
#                expect = target-num[i]-num[j]
#                m = j+1
#                n = len(num)-1
#                while m<n:
#                    if num[m]+num[n]<expect:
#                        m += 1
#                    elif num[m]+num[n]>expect:
#                        n -= 1
#                    else:
#                        temp = sorted([num[i], num[j], num[m], num[n]])
#                        result.append(temp) if temp not in result else None
#                        while m<n and num[m+1]==num[m]:
#                            m += 1
#                        while m<n and num[n-1]==num[n]:
#                            n -= 1
#                        m += 1
#                        n -= 1
#        return result



class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        if len(num)<4:
            return[]
        if len(num)==4:
            return [sorted(num)] if sum(num)==target else []
        num.sort()
        pairs = []
        filter_num = []
        count = 0
        l = [num[0]]
        dic = {}
        result = []
        print num
        for t in range(1, len(num)):
            if num[t]==num[t-1]:
                count += 1
            else:
                count = 0
            if count<4:
                l.append(num[t])
        num = l[:]
        print num
        for i in range(len(num)-1):
            for j in range(i+1, len(num)):
                pairs.append((i, j))
        for pair in pairs:
            temp = target-num[pair[0]]-num[pair[1]]
            if temp in dic:
                dic[temp].append(pair)
            else:
                dic[temp] = [pair]
        for pair in pairs:
            temp = num[pair[0]] + num[pair[1]]
            if temp in dic:
                for d in dic[temp]:
                    if pair[1]<d[0]:
                        t = sorted([num[pair[0]], num[pair[1]], num[d[0]], num[d[1]]])
                        result.append(t) if t not in result else None
        return result

        




t = Solution()
print t.fourSum([1,1,1,1,1,1,1,1,0,-1,0,-2,2], 0)

