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
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        from sortedcontainers import SortedList
        sl = SortedList()
        p = head
        while p:
            sl.add(p.val)
            p = p.next

        ans, prev = None, None
        p = head
        while p:
            if p.val == sl[-1]:
                if prev is None:
                    ans = p
                    prev = p
                else:
                    prev.next = p
                    prev = p
            sl.remove(p.val)
            p = p.next
        if prev:
            prev.next = None
        return ans


if __name__ == '__main__':
    pass
