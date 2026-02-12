#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minCostToTravelOnDays(self, days: List[int], tickets: List[List[int]]) -> int:
        n = len(days)
        inf = 1 << 62
        costs = [inf] * (n + 1)
        costs[0] = 0
        for i in range(n):
            d = days[i]
            for duration, price in tickets:
                t = (d + duration - 1)
                s, e = i + 1, n - 1
                while s <= e:
                    m = (s + e) // 2
                    if t >= days[m]:
                        s = m + 1
                    else:
                        e = m - 1
                costs[s] = min(costs[s], costs[i] + price)
        return costs[n]


true, false, null = True, False, None
cases = [
    ([1, 2, 3, 4], [[1, 3], [2, 5], [3, 7]], 10),
    ([1, 4, 5], [[1, 4], [5, 6], [2, 5]], 6),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minCostToTravelOnDays, cases)

if __name__ == '__main__':
    pass
