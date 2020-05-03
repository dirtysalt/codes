#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.it = iterator
        self.buf = None

    def fill(self):
        if self.buf is None:
            if self.it.hasNext():
                self.buf = self.it.next()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        self.fill()
        return self.buf

    def next(self):
        """
        :rtype: int
        """
        self.fill()
        x = self.buf
        self.buf = None
        return x

    def hasNext(self):
        """
        :rtype: bool
        """
        self.fill()
        return self.buf is not None
