#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class MyCalendarThree:

    def __init__(self):
        self.dates = []

    def book(self, start: int, end: int) -> int:
        self.dates.append((start, 1))
        self.dates.append((end, -1))
        self.dates.sort()

        res = 0
        ans = 0
        for t, d in self.dates:
            res += d
            ans = max(ans, res)
        return ans
