#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
'''

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        if len(intervals)<2:
            return intervals
        interval_cmp = lambda x, y : cmp(x.start, y.start) 
        intervals.sort(interval_cmp)
        i = 1
        j = 1
        while j < len(intervals):
            if intervals[i-1].end>=intervals[j].start:
                intervals[i-1].end = max(intervals[i-1].end, intervals[j].end)
                j += 1
            else:
                intervals[i], intervals[j] = intervals[j], intervals[i]
                i += 1
                j += 1
        return intervals[:i]


intervals = [Interval(1,4), Interval(2,3)]
t = Solution()
print t.merge(intervals)

