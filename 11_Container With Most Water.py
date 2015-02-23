#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.
'''

# 这个题的题意要理解清楚。。。

class Solution:
    # @return an integer
    def maxArea(self, height):
        result = 0
        i, j = 0, len(height)-1
        while i<j:
            result = max(result, (j-i)*min(height[i], height[j]))
            if height[i]<height[j]:
                i += 1
            else:
                j -= 1
        return result
