#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Heap:
    def __init__(self, cap):
        self.data = [None]
        self.cap = cap

    def adjust1(self, idx):
        c0 = 2 * idx
        c1 = 2 * idx + 1
        n = len(self.data)
        swap = None

        if c1 < n and self.data[c1] < self.data[idx]:
            if self.data[c0] < self.data[c1]:
                swap = c0
            else:
                swap = c1
        elif c0 < n and self.data[c0] < self.data[idx]:
            swap = c0

        if swap:
            n0, n1 = self.data[swap], self.data[idx]
            n0.heap_idx = idx
            n1.heap_idx = swap
            self.data[swap], self.data[idx] = n1, n0
        return swap

    def adjust(self, idx):
        n = len(self.data)
        p = idx
        while p < n:
            swap = self.adjust1(p)
            if swap is None:
                break
            p = swap
        p = idx // 2
        while p:
            swap = self.adjust1(p)
            if swap is None:
                break
            p = p // 2

    def append(self, node):
        evicted = None
        n = len(self.data)
        if (n - 1) == self.cap:
            evicted = self.data[1]
            node.heap_idx = 1
            self.data[1] = node
            self.adjust(1)
        else:
            node.heap_idx = n
            self.data.append(node)
            self.adjust(n)
        return evicted


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.op_count = 0
        self.op_idx = 0
        self.heap_idx = 0

    def inc_count(self, op_idx):
        self.op_count += 1
        self.op_idx = op_idx

    def __lt__(self, other):
        if self.op_count != other.op_count:
            return self.op_count < other.op_count
        return self.op_idx < other.op_idx


class LFUCache:
    """
    @param: capacity: An integer
    """

    def __init__(self, capacity):
        # do intialization if necessary
        self.node_map = dict()
        self.node_heap = Heap(capacity)
        self.global_op_idx = 1

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """

    def inc_global_op_idx(self):
        ts = self.global_op_idx
        self.global_op_idx += 1
        return ts

    def set(self, key, value):
        # write your code here
        op_idx = self.inc_global_op_idx()
        node = self.node_map.get(key)
        if node is not None:
            node.inc_count(op_idx)
            node.value = value
            self.node_heap.adjust(node.heap_idx)
            return

        node = Node(key, value)
        node.inc_count(op_idx)
        evicted = self.node_heap.append(node)
        if evicted:
            del self.node_map[evicted.key]
        self.node_map[node.key] = node

    """
    @param: key: An integer
    @return: An integer
    """

    def get(self, key):
        # write your code here
        op_idx = self.inc_global_op_idx()
        node = self.node_map.get(key)
        if node is not None:
            node.inc_count(op_idx)
            self.node_heap.adjust(node.heap_idx)
            return node.value
        return -1
