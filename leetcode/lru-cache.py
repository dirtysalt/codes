#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class LRUCache(object):
    class Node(object):
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

        def __str__(self):
            return '(%s, %s)' % (self.key, self.value)

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.qh = LRUCache.Node(-1, -1)
        self.qt = LRUCache.Node(-1, -1)
        self.qh.next = self.qt
        self.qt.prev = self.qh
        self.d = {}
        self.cap = capacity

    def __str__(self):
        xs = []
        head = self.qh.next
        while not head is self.qt:
            xs.append(head)
            head = head.next
        return ','.join(map(str, xs))

    def _take(self, n):
        # take it up
        pn = n.prev
        nn = n.next
        pn.next = nn
        nn.prev = pn

    def _put(self, n):
        # and put it down.
        pn = self.qt.prev
        pn.next = n
        n.prev = pn
        n.next = self.qt
        self.qt.prev = n

    def _evict(self):
        # print('--- evict ---')
        n = self.qh.next
        nn = n.next
        self.qh.next = nn
        nn.prev = self.qh
        key = n.key
        # print('evict %d' % key)
        del self.d[key]

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.d:
            n = self.d[key]
            self._take(n)
            self._put(n)
            return n.value
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key not in self.d:
            if len(self.d) == self.cap:
                self._evict()
            n = LRUCache.Node(key, value)
            self.d[key] = n
        else:
            n = self.d[key]
            self._take(n)
            n.value = value
        self._put(n)
