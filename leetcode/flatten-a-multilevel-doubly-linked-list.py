#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        root = Node(None, None, None, None)

        def visit(head, last):
            while head:
                tmp = head.next
                last.next = head
                head.prev = last
                last = visit(head.child, head)
                # HERE!!!
                head.child = None
                head = tmp
            return last

        visit(head, root)
        ans = root.next
        if ans:
            ans.prev = None
        return ans
