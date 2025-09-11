#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = ListNode()
        cur = tmp
        nums = set(nums)
        while head:
            if head.val not in nums:
                cur.next = head
                cur = head
            head = head.next
        cur.next = None
        return tmp.next


if __name__ == '__main__':
    pass
