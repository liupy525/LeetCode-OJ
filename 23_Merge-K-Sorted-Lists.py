#!/usr/local/env python
# -*- coding: utf-8 -*-

'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
'''

import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from heapq import heappush, heappop
class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        heap = []
        for i in lists:
            p = i
            while p:
                heappush(heap, (p.val, p))
                p = p.next
        head = ListNode(-1)
        p = head
        while heap:
            p.next = heappop(heap)[1]
            p = p.next
        p.next = None
        return head.next






#class Solution:
#    # @param a list of ListNode
#    # @return a ListNode
#    def mergeKLists(self, lists):
#        lists = [ t for t in lists if t ]
#        head = ListNode(-1)
#        p = head
#        #while not self.emptyLists(lists):
#        while lists!=[]:
#            vals = [ t.val for t in lists]
#            minvalindex = vals.index(sorted(vals)[0])
#            p.next = lists[minvalindex]
#            p = p.next
#            if lists[minvalindex].next:
#                lists[minvalindex] = lists[minvalindex].next 
#            else:
#                lists.pop(minvalindex)
#        return head.next
#    def emptyLists(self, lists):
#        return [ i for i in lists if i ]==[]



# initialize lists
lists = []
for i in range(5):
    dummy = ListNode(0)
    p = dummy
    temp = [ random.randint(0, 100) for i in range(random.randint(4, 10)) ]
    temp.sort()
    for i in temp:
        p.next = ListNode(i)
        p = p.next
    lists.append(dummy.next)

for i in range(len(lists)):
    p = lists[i]
    print 'No.', i, ':::', '\t',
    while p:
        print p.val, '->',
        p = p.next
    print 

# start test
#lists = [None, ListNode(0)]
#lists = [None]
t = Solution()
p = t.mergeKLists(lists)
#p = t.mergeKLists([None, None])

# print result
while p:
    print p.val, '->',
    p = p.next
        

