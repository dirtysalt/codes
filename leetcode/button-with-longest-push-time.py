#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        ans, value = events[0]
        for i in range(1, len(events)):
            (_, t0) = events[i - 1]
            (idx, t1) = events[i]
            t = t1 - t0
            if t > value or (t == value and idx < ans):
                ans = idx
                value = t
        return ans


if __name__ == '__main__':
    pass
