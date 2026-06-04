#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        p = head
        while p:
            p2 = p.next
            if not p2: break
            v = gcd(p.val, p2.val)
            n = ListNode(v)
            p.next = n
            n.next = p2
            p = p2
        return head


if __name__ == '__main__':
    pass
