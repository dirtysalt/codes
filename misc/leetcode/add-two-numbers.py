#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        prev = None
        flag = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            v = v1 + v2 + flag
            flag = v / 10
            v = v % 10
            node = ListNode(v)

            if not head:
                head = node
            else:
                prev.next = node
            prev = node

        if flag:
            node = ListNode(flag)
            prev.next = node

        return head
