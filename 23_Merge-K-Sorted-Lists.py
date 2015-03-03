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

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        temp_lists = []
        for i in range(len(lists)):
            if lists[i]:
                temp_lists.append(lists[i])
        lists = temp_lists
        result = ListNode(0)
        p = result
        while lists:
            val = [ lists[i].val for i in range(len(lists)) ]
            val.sort()
            min_val = val.index(val[0])
            while lists[min_val].next and lists[min_val].next.val<val[1]:
                p.next = lists[min_val]
                lists[min_val] = lists[min_val].next
                p = p.next
            if lists[min_val].next==None:
                lists.pop(min_val)
        p.next = None
        return result.next


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
t = Solution()
p = t.mergeKLists(lists)
#p = t.mergeKLists([None, None])

# print result
while p:
    print p.val, '->',
    p = p.next
        

