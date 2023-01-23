#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteListNode(self, head: ListNode) -> ListNode:
        root = head

        while head:
            n = head.next
            if n:
                n2 = n.next
                head.next = n2
                head = n2
            else:
                break

        return root


if __name__ == '__main__':
    pass
