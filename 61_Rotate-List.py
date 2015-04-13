#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if not head or k==0 or not head.next:
            return head

        l = 0
        tmp = head
        while tmp:
            tmp = tmp.next
            l += 1
        k = k%l
        if k==0:
            return head

        dummy = ListNode(0)
        dummy.next = head
        m, n = head, dummy
        for i in xrange(k):
            if not m:
                return head
            p = m
            m = m.next
        while m:
            p = m
            m, n = m.next, n.next
        if n==dummy:
            return dummy.next
        else:
            p.next = head
            r = n.next
            n.next = None
            return r

head = ListNode(1)
p = head
for i in range(1):
    p.next = ListNode(i+2)
    p.next.next = None
    p = p.next

t = Solution()
tmp = t.rotateRight(head, 3)
while tmp:
    print tmp.val
    tmp = tmp.next




