#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLL:
    def __int__(self):
        dummy = Node(None)
        self.head = dummy
        self.tail = dummy

    def empty(self):
        return self.head is self.tail

    def append(self, node):
        node.prev = self.tail
        node.next = None
        self.tail.next = node
        self.tail = node

    def remove(self, node):
        prev = node.prev
        next = node.next
        if next:
            next.prev = prev
        else:
            self.tail = prev
        prev.next = next
        return node, next
