#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.op_count = 1
        self.prev = None
        self.next = None


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


class DoublyLLMap:
    def __init__(self):
        self.map = {}

    def remove_node(self, node):
        op_count = node.op_count
        dll = self.map[op_count]
        dll.remove_node(node)
        if dll.is_empty():
            del self.map[op_count]

    def add_node(self, node):
        op_count = node.op_count
        if op_count not in self.map:
            self.map[op_count] = DoublyLL()
        dll = self.map[op_count]
        dll.append_node(node)

    def evict_node(self):
        min_op_count = min(self.map.keys())
        dll = self.map[min_op_count]
        node = dll.pop_node()
        if dll.is_empty():
            del self.map[min_op_count]
        return node


class LFUCache:
    """
    @param: capacity: An integer
    """

    def __init__(self, capacity):
        # do intialization if necessary
        self.node_map = dict()
        self.dll_map = DoublyLLMap()
        self.cap = capacity

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """

    def set(self, key, value):
        # write your code here
        node = self.node_map.get(key)
        if node is not None:
            node.value = value
            self.dll_map.remove_node(node)
            node.op_count += 1
            self.dll_map.add_node(node)
            return

        node = Node(key, value)
        if len(self.node_map) == self.cap:
            evicted = self.dll_map.evict_node()
            del self.node_map[evicted.key]
        self.dll_map.add_node(node)
        self.node_map[node.key] = node

    """
    @param: key: An integer
    @return: An integer
    """

    def get(self, key):
        # write your code here
        node = self.node_map.get(key)
        if node is not None:
            self.dll_map.remove_node(node)
            node.op_count += 1
            self.dll_map.add_node(node)
            return node.value
        return -1
