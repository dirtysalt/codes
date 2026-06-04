#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        res = ListNode(0)
        res.next = head
        prev = res

        for i in range(0, m - 1):
            prev = prev.next
            head = head.next

        tail = head
        pp = head
        head = head.next

        for i in range(m, n):
            t = head.next
            head.next = pp
            pp = head
            head = t

        tail.next = head
        prev.next = pp
        return res.next
