#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """

        p = root
        n = 0
        while p:
            n += 1
            p = p.next

        size = n // k
        reminder = n % k
        ans = []

        p = root
        for i in range(k):
            exp_size = size + (1 if i < reminder else 0)
            head = p
            prev = None
            for j in range(exp_size):
                if p:
                    prev = p
                    p = p.next
            if prev: prev.next = None
            ans.append(head)
        return ans
