#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        r0 = ListNode(-1)
        p0 = r0
        r1 = ListNode(-1)
        p1 = r1

        while head:
            if head.val < x:
                p0.next = head
                p0 = head
            else:
                p1.next = head
                p1 = head
            head = head.next
        p0.next = r1.next
        p1.next = None
        return r0.next
