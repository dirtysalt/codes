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
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        pos = []
        p = 1
        while head:
            n = head.next
            if n and n.next:
                n2 = n.next
                if (n.val > head.val and n.val > n2.val) or (n.val < head.val and n.val < n2.val):
                    pos.append(p)
            p += 1
            head = n

        ans = [-1, -1]
        if len(pos) >= 2:
            m = 1 << 30
            for i in range(1, len(pos)):
                m = min(m, pos[i] - pos[i - 1])
            ans[0] = m
            ans[1] = pos[-1] - pos[0]

        return ans


if __name__ == '__main__':
    pass
