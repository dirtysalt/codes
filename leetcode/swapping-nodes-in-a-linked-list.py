#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        size = 0
        p = head
        while p:
            size += 1
            p = p.next

        k2 = (size + 1) - k
        if k2 < k:
            k = k2

        p = head
        p2 = head
        for _ in range(k - 1):
            p2 = p2.next

        p3 = p2
        while p3.next:
            p3 = p3.next
            p = p.next

        # swap p and p2
        p.val, p2.val = p2.val, p.val
        return head
