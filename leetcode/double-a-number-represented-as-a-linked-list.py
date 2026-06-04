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
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def walk(root):
            root.val *= 2

            if not root.next:
                return

            walk(root.next)
            if root.next.val >= 10:
                root.val += 1
                root.next.val -= 10

        walk(head)
        if head.val >= 10:
            root = ListNode(1)
            head.val -= 10
            root.next = head
            head = root
        return head


if __name__ == '__main__':
    pass
