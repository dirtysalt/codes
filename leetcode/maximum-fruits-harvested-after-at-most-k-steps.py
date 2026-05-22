#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import bisect
from typing import List


class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        fruits.sort(key=lambda x: tuple(x))
        n = len(fruits)

        pos = [x[0] for x in fruits]
        amount = [x[1] for x in fruits]

        acc = [0] * (n + 1)
        for i in range(n):
            acc[i + 1] = acc[i] + amount[i]

        ans = 0
        for i in range(n):
            p = pos[i]
            rest = k - abs(startPos - p)
            if rest < 0: continue
            # search backward
            if True:
                p2 = p - rest
                j = bisect.bisect_left(pos, p2)
                assert j >= 0
                a = acc[i + 1] - acc[j]
                ans = max(ans, a)

            # search forward
            if True:
                p2 = p + rest
                j = bisect.bisect_right(pos, p2) - 1
                assert j < n
                a = acc[j + 1] - acc[i]
                ans = max(ans, a)
        return ans


if __name__ == '__main__':
    pass
