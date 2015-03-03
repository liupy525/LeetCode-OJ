#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        dummy = p0 = ListNode(0)
        dummy.next = head
        while p0.next and p0.next.next:
            p1, p2 = p0.next, p0.next.next
            p0.next, p1.next, p2.next = p2, p2.next, p1
            p0 = p0.next.next
        return dummy.next

