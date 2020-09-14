#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Heap:
    def __init__(self):
        self.data = [None]

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
        # down path.
        p = idx
        while p < n:
            swap = self.adjust1(p)
            if swap is None:
                break
            p = swap
        # up path.
        p = idx // 2
        while p:
            swap = self.adjust1(p)
            if swap is None:
                break
            p = p // 2

    def top(self):
        return self.data[1]


class Node:
    def __init__(self, value=None):
        self.value = value
        self.heap_idx = 0

    def __lt__(self, other):
        return self.value > other.value


class DoublyLL:
    def __init__(self):
        dummy = Node()
        self.head = dummy
        self.tail = dummy

    def is_empty(self):
        return self.head is self.tail

    def append_node(self, node):
        node.next = None
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    def pop_node(self):
        node = self.head.next
        self.head.next = node.next
        if node.next:
            node.next.prev = self.head
        else:
            self.tail = self.head
        return node

    def remove_node(self, node):
        pn = node.prev
        nn = node.next
        pn.next = nn
        if nn:
            nn.prev = pn
        else:
            self.tail = pn


class Solution:
    """
    @param: nums: A list of integers
    @param: k: An integer
    @return: The maximum number inside the window at each moving
    """

    def maxSlidingWindow(self, nums, k):
        # write your code here
        if k == 0: return []
        dll = DoublyLL()
        heap = Heap()
        for i in range(k):
            value = nums[i]
            node = Node(value)
            node.heap_idx = i + 1
            dll.append_node(node)
            heap.data.append(node)
            heap.adjust(node.heap_idx)

        res = []
        res.append(heap.top().value)
        for i in range(k, len(nums)):
            old_node = dll.pop_node()
            old_value = old_node.value
            new_value = nums[i]
            new_node = Node(new_value)
            dll.append_node(new_node)

            heap.data[old_node.heap_idx] = new_node
            new_node.heap_idx = old_node.heap_idx
            heap.adjust(new_node.heap_idx)
            res.append(heap.top().value)

        return res
