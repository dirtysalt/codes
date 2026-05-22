#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        res = ListNode('dummy')
        prev = res
        while head:
            if head.next is not None:
                cont = head.next.next
                (x, y) = (head, head.next)
                y.next = x
                x.next = cont
                prev.next = y
                prev = x
                head = cont
            else:
                prev.next = head
                break
        return res.next
