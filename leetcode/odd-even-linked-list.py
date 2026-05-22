#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        h0 = head
        h1 = head.next
        if not h1:
            return h0

        t0, t1 = h0, h1
        p = h1.next
        idx = 2
        while p:
            if idx % 2 == 0:
                t0.next = p
                t0 = p
            else:
                t1.next = p
                t1 = p
            idx += 1
            p = p.next
        t1.next = None
        t0.next = h1
        return h0
