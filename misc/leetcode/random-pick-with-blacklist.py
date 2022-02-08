#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import random
import bisect
from typing import List
import array

class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        self.rnd = random.Random(42)
        blacklist.sort()

        intervals = []
        sizes = []
        last = 0
        for x in blacklist:
            to = x - 1
            if to >= last:
                intervals.append((last, to))
            last = x + 1

        if last < N:
            intervals.append((last, N-1))

        sizes = [(to - last + 1) for (last, to) in intervals]
        for i in range(1, len(sizes)):
            sizes[i] += sizes[i-1]

        # print(sizes, intervals)
        self.sizes = sizes
        self.intervals = intervals

    def pick(self) -> int:
        sizes, intervals = self.sizes, self.intervals
        rnd = self.rnd.randint(0, sizes[-1]-1)
        idx = bisect.bisect_right(sizes, rnd)
        # print(rnd, idx)
        (last, to) = self.intervals[idx]
        return to + 1 - (sizes[idx] - rnd)
