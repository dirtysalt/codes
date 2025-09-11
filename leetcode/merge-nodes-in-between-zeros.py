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
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        root = dummy
        value = 0
        while head:
            if head.val == 0:
                if value != 0:
                    root.next = ListNode(value)
                    root = root.next
                value = 0
            else:
                value += head.val
            head = head.next
        if value != 0:
            root.next = ListNode(value)
            root = root.next
        root.next = None
        return dummy.next


if __name__ == '__main__':
    pass
