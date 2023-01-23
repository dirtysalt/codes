#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        last = {}
        d = 0
        for t in tasks:
            if t in last:
                wait = max(0, last[t] + space - d)
                d += wait
            d += 1
            last[t] = d
        return d


if __name__ == '__main__':
    pass
