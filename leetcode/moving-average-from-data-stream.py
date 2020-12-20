#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from collections import deque


class MovingAverage:
    """
    @param: size: An integer
    """

    def __init__(self, size):
        # do intialization if necessary
        self.queue = deque(maxlen=size)
        self.mvacc = 0

    """
    @param: val: An integer
    @return:
    """

    def next(self, val):
        # write your code here
        if len(self.queue) == self.queue.maxlen:
            pop = self.queue.popleft()
            self.mvacc -= pop
        self.mvacc += val
        self.queue.append(val)
        return self.mvacc / len(self.queue)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)
