#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        st = []
        p = head
        while p:
            st.append(p)
            p = p.next
        n = len(st)
        (s, e) = (0, n - 1)
        dummy = ListNode(-1)
        prev = dummy
        while s <= e:
            x = st[s]
            y = st[e]
            x.next = y
            y.next = None
            prev.next = x
            prev = y
            s += 1
            e -= 1
        prev.next = None
