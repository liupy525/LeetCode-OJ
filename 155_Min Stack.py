#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''

class MinStack:
    def __init__(self):
        self.l = []
        self.mi = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
       self.l.append(x) 
       if not self.mi:
           self.mi.append(x)
       elif self.mi[-1]>=x:
            self.mi.append(x)

    # @return nothing
    def pop(self):
        t = self.l.pop()
        if self.mi[-1]==t:
            self.mi.pop()

    # @return an integer
    def top(self):
        return self.l[-1]

    # @return an integer
    def getMin(self):
        return self.mi[-1]
        
