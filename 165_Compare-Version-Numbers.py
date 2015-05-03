#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Compare two version numbers version1 and version1.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
'''

class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        v1 = [ int(i) for i in version1.split('.') ]
        v2 = [ int(i) for i in version2.split('.') ]
        lv1 = len(v1)
        lv2 = len(v2)
        if lv1>lv2:
            v2 += [0] * (lv1-lv2)
        elif lv2>lv1:
            v1 += [0] * (lv2-lv1)
        for t in range(len(v1)):
            if v1[t] == v2[t]:
                continue
            if v1[t] > v2[t]:
                return 1
            elif v1[t] < v2[t]:
                return -1
        return 0


t = Solution()
print t.compareVersion('01.4.1', '1.4.1')
