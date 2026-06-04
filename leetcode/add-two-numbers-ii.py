#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#
#         def rev(p):
#             prev = None
#             while p:
#                 p2 = p.next
#                 p.next = prev
#                 prev = p
#                 p = p2
#             return prev
#
#         if l1 is None:
#             return l2
#         if l2 is None:
#             return l1
#
#         p1 = rev(l1)
#         p2 = rev(l2)
#
#         pp1, pp2, head = None, None, None
#         carry = 0
#         while p1 or p2:
#             a = p1.val if p1 else 0
#             b = p2.val if p2 else 0
#             if p1:
#                 tmp = p1.next
#                 p1.next = pp1
#                 pp1 = p1
#                 p1 = tmp
#             if p2:
#                 tmp = p2.next
#                 p2.next = pp2
#                 pp2 = p2
#                 p2 = tmp
#             carry += (a + b)
#             node = ListNode(carry % 10)
#             carry //= 10
#             node.next = head
#             head = node
#         if carry:
#             node = ListNode(carry)
#             node.next = head
#             head = node
#         return head


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        self.st1 = []
        self.st2 = []
        if l2 is None: return l1
        if l1 is None: return l2
        while l1:
            self.st1.append(l1.val)
            l1 = l1.next
        while l2:
            self.st2.append(l2.val)
            l2 = l2.next
        head = None
        carry = 0
        while self.st1 or self.st2:
            a = 0
            if self.st1:
                a = self.st1[-1]
                self.st1.pop()
            b = 0
            if self.st2:
                b = self.st2[-1]
                self.st2.pop()
            carry += (a + b)
            node = ListNode(carry % 10)
            carry //= 10
            node.next = head
            head = node
        if carry:
            node = ListNode(carry)
            node.next = head
            head = node
        return head
