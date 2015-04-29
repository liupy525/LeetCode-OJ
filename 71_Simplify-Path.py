#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
'''

class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        p = path.split('/')
        path = []
        for i in p:
            if i and i!='.':
                path.append(i)
        r = []
        for i in range(len(path)):
            if path[i]=='..':
                if r:
                    r.pop()
            else:
                r.append(path[i])
        
        return '/'+'/'.join(r)

path =  "/a/./b/../../c/"
path = "/../"
t = Solution()
print  t.simplifyPath(path)
