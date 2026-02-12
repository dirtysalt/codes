#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        x = head
        n = 0
        pp = None
        while x:
            n += 1
            pp = x
            x = x.next

        if n == 0: return head
        k = k % n
        if k == 0: return head

        x = head
        for i in range(0, n - k - 1):
            x = x.next
        p = x.next
        pp.next = head
        x.next = None
        return p
