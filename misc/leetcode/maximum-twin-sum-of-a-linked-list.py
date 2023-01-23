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
    def pairSum(self, head: Optional[ListNode]) -> int:
        values = []
        while head:
            values.append(head.val)
            head = head.next

        i, j = 0, len(values) - 1
        ans = 0
        while i < j:
            res = values[i] + values[j]
            i += 1
            j -= 1
            ans = max(ans, res)
        return ans


if __name__ == '__main__':
    pass
