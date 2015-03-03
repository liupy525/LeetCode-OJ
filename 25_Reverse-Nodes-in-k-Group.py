#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
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
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        p = [ None for i in range(k+1) ]
        p[0] = dummy
        try:
            while 1:
                # initialize p
                for i in range(k):
                    p[i+1] = p[i].next

                # get the order after changing 
                l = [ p[-1], p[-1].next ]
                l.extend( [ p[i+1] for i in range(k-1) ] )

                # put the changed order into the p[i].next 
                for i in range(len(p)):
                    p[i].next = l[i]

                # ready for the next change
                for i in range(k):
                    p[0] = p[0].next
        except:
            return dummy.next

# initialize head
dummy = ListNode(0)
p = dummy
for i in range(1, 10):
    p.next = ListNode(i)
    p = p.next
head = dummy.next

# start test
t = Solution()
p = t.reverseKGroup(head, 3)

# print result
while p:
    print p.val, '->',
    p = p.next
        
