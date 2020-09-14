#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def merge(self, p0, p1):
        # print nodes_to_list(p0), nodes_to_list(p1)
        dm = ListNode(-1)
        pp = dm
        while p0 and p1:
            if p0.val < p1.val:
                pp.next = p0
                pp = p0
                p0 = p0.next
            else:
                pp.next = p1
                pp = p1
                p1 = p1.next
        if p0:
            pp.next = p0
        if p1:
            pp.next = p1
        while pp.next:
            pp = pp.next
        return (dm.next, pp)

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        n = 0
        p = head
        while p:
            n += 1
            p = p.next

        dummy = ListNode(-1)
        dummy.next = head
        i = 1
        while (1 << (i - 1)) <= n:
            prev = dummy
            p = dummy.next

            while p:
                p0 = p
                for j in range((1 << (i - 1)) - 1):
                    if not p0.next: break
                    p0 = p0.next
                p1 = p0.next
                p0.next = None

                nextp = None
                if p1:
                    p2 = p1
                    for j in range((1 << (i - 1)) - 1):
                        if not p2.next: break
                        p2 = p2.next
                    nextp = p2.next
                    p2.next = None

                (h, t) = self.merge(p, p1)
                # print nodes_to_list(h)
                prev.next = h
                prev = t
                p = nextp
            i += 1
            prev.next = None
            # print '>>>', nodes_to_list(dummy.next), i
        return dummy.next


def list_to_nodes(xs):
    d = ListNode(-1)
    p = d
    for x in xs:
        p.next = ListNode(x)
        p = p.next
    p.next = None
    return d.next


def nodes_to_list(n):
    xs = []
    while n:
        xs.append(n.val)
        n = n.next
    return xs


if __name__ == '__main__':
    s = Solution()
    print(nodes_to_list(s.sortList(list_to_nodes([5, 4, 3, 1, 2, ]))))
