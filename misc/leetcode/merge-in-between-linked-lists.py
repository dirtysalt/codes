#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        def findKthPrev(l, k):
            for _ in range(k - 1):
                l = l.next
            return l

        def tail(l):
            while l.next:
                l = l.next
            return l

        ha = findKthPrev(list1, a)
        ta = findKthPrev(list1, b)
        ta = ta.next.next

        hb = list2
        tb = tail(list2)

        ha.next = hb
        tb.next = ta

        return list1
