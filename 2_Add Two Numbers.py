#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        n1 = 0
        n2 = 0
        re = 0
        i  = 0
        pointer = l1
        while pointer:
            n1 += pointer.val * 10 ** i
            i += 1
            pointer = pointer.next
        i  = 0
        pointer = l2
        while pointer:
            n2 += pointer.val * 10 ** i
            i += 1
            pointer = pointer.next
        re = n1 + n2
        m, n = re/10, re%10
        first = ListNode(n)
        l = first
        while m:
            m, n = m/10, m%10
            t = ListNode(n)
            l.next = t
            l = l.next
        return first


        

