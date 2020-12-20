#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from queue import PriorityQueue as PQ


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        pq = PQ()
        n = len(lists)
        res = ListNode('head')
        prev = res
        for i in range(0, n):
            if lists[i] is None: continue
            pq.put((lists[i].val, lists[i]))

        while not pq.empty():
            (v, node) = pq.get()
            prev.next = ListNode(v)
            prev = prev.next
            node = node.next
            if node is not None:
                pq.put((node.val, node))

        return res.next
