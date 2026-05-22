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
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        size = 0
        while head:
            size += 1
            head = head.next
        size = size // 2

        pp = dummy
        while size:
            pp = pp.next
            size -= 1

        x = pp.next.next if pp.next else None
        pp.next = x
        return dummy.next


if __name__ == '__main__':
    pass
