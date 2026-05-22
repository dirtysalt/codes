#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import functools
from typing import List


class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        INF = 1 << 30
        n = len(prices)

        @functools.cache
        def search(i, j):
            if i == (n + 1): return 0
            ans = INF
            if i <= j:
                c = search(i + 1, j)
                ans = min(ans, c)

            c = prices[i - 1] + search(i + 1, min(max(j, 2 * i), n))
            ans = min(ans, c)
            return ans

        ans = search(1, 0)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([3, 1, 2], 4),
    ([1, 10, 1, 1], 2),
]

aatest_helper.run_test_cases(Solution().minimumCoins, cases)

if __name__ == '__main__':
    pass
