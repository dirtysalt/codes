#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        res = ListNode('dummy')
        prev = res

        while head:
            st = []
            for i in range(k):
                if head is None: break
                st.append(head)
                head = head.next

            if len(st) != k:
                prev.next = st[0]
                break

            st = st[::-1]
            for i in range(1, len(st)):
                st[i - 1].next = st[i]
            prev.next = st[0]
            prev = st[-1]
            st[-1].next = None

        return res.next


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def list_to_nodes(xs):
    nodes = [ListNode(x) for x in xs]
    for i in range(1, len(nodes)):
        nodes[i - 1].next = nodes[i]
    return nodes[0]


def nodes_to_list(nodes):
    xs = []
    while nodes:
        xs.append(nodes.val)
        nodes = nodes.next
    return xs


if __name__ == '__main__':
    s = Solution()
    print(nodes_to_list(s.reverseKGroup(list_to_nodes([1, 2]), 2)))
