#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        while head:
            p = head
            head = head.next

            pp = dummy
            while pp.next:
                if p.val > pp.next.val:
                    pp = pp.next
                else:
                    break
            p.next = pp.next
            pp.next = p
        return dummy.next
