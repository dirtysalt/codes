#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List, Optional
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode()
        prev = root
        k = 1
        st = []
        while head:
            i = k
            k += 1
            st.clear()
            while i > 0:
                st.append(head)
                head = head.next
                i -= 1
                if head is None:
                    break

            if len(st) % 2 == 0:
                st = st[::-1]
            for x in st:
                prev.next = x
                prev = x

        prev.next = None
        return root.next


if __name__ == '__main__':
    pass
