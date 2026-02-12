#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: the first Node
    @return: the answer after plus one
    """

    def plusOne(self, head):
        # Write your code here

        # reverse it.
        new_head = None
        while head:
            temp = head.next
            head.next = new_head
            new_head = head
            head = temp

        # reverse back, while + 1.
        head = new_head
        carry = 1
        new_head = None
        while head:
            temp = head.next
            head.next = new_head
            new_head = head
            head = temp
            val = new_head.val + carry
            carry = val // 10
            new_head.val = val % 10
        if carry:
            node = ListNode(carry)
            node.next = new_head
            new_head = node
        return new_head
