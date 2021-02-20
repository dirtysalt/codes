#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import random


class Solution:
    def __init__(self, head):
        """
        @param head The linked list's head.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        p = self.head
        matched = 0
        value = None
        while p:
            matched += 1
            if random.randint(0, matched - 1) == 0:
                value = p.val
            p = p.next
        return value
