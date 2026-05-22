#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class StreamStatistics:
    def __init__(self):
        self.sum = 0
        self.n = 0
        self.x2 = 0

    def add(self, x):
        self.sum += x
        self.n += 1
        self.x2 += x * x

    def rem(self, x):
        self.sum -= x
        self.n -= 1
        self.x2 -= x * x

    def avg(self):
        return self.sum / self.n

    def dev(self):
        m = self.avg()
        t = self.x2 - self.sum * self.sum / self.n
        return t / self.n


class Solution:
    def honeyQuotes(self, handle: List[List[int]]) -> List[float]:
        ss = StreamStatistics()
        ans = []

        for ev in handle:
            if ev[0] == 1:
                ss.add(ev[1])
            elif ev[0] == 2:
                ss.rem(ev[1])
            elif ev[0] == 3:
                if ss.n == 0:
                    ans.append(-1.0)
                else:
                    ans.append(ss.avg())
            elif ev[0] == 4:
                if ss.n == 0:
                    ans.append(-1.0)
                else:
                    ans.append(ss.dev())
        return ans


true, false, null = True, False, None
cases = [
    (
        [[1, 1], [1, 2], [1, 3], [1, 2], [3], [4], [2, 1], [2, 2], [2, 3], [3], [4]],
        [2.00000, 0.50000, 2.00000, 0.00000]),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().honeyQuotes, cases)

if __name__ == '__main__':
    pass
