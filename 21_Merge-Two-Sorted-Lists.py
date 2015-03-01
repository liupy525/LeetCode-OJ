#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        result = ListNode(-1)
        l3 = result
        while l1 and l2:
            if l1.val<l2.val:
                l1, l3.next = l1.next, l1
            else:
                l2, l3.next = l2.next, l2
            l3 = l3.next
        l3.next = l1 and l1 or l2
        return result.next
        


