#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head
        res = head
        prev = res
        head = head.next
        while head:
            if head.val != prev.val:
                prev.next = head
                prev = head
            head = head.next
        prev.next = None
        return res
