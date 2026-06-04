#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        sz = 0
        p = head
        while p:
            sz += 1
            p = p.next

        st = []
        p = head
        for i in range(sz // 2):
            st.append(p.val)
            p = p.next

        if sz % 2 == 1:
            p = p.next

        while p:
            if st[-1] != p.val:
                return False
            st.pop()
            p = p.next
        return True
