#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import bisect


class MyCalendar:

    def __init__(self):
        self.xs = []
        self.ys = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        i = bisect.bisect_left(self.xs, start)
        # compare to self.ys[i-1] and self.xs[i]
        if (i - 1) >= 0:
            if start < self.ys[i - 1]:
                return False
        if i < len(self.xs):
            if end > self.xs[i]:
                return False
        self.xs.insert(i, start)
        self.ys.insert(i, end)
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
