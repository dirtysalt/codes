#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def size(x):
            c = 0
            while x:
                c += 1
                x = x.next
            return c

        asize = size(headA)
        bsize = size(headB)
        if asize > bsize:
            headA, headB = headB, headA
            asize, bsize = bsize, asize

        delta = bsize - asize
        for i in range(delta):
            headB = headB.next

        while headA and headB and headA != headB:
            headA = headA.next
            headB = headB.next

        if headA == headB:
            return headA
        return None
