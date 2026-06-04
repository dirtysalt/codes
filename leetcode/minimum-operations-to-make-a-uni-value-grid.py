#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        from collections import Counter
        cnt = Counter()
        for R in grid:
            for C in R:
                cnt[C] += 1

        keys = list(cnt.keys())
        keys.sort()
        n = len(keys)
        values = [0] * n
        for i in range(n):
            values[i] += cnt[keys[i]]

        # check ok
        for i in range(1, n):
            d = keys[i] - keys[i - 1]
            if d % x != 0:
                return -1

        res = 0
        for i in range(1, n):
            d = keys[i] - keys[0]
            res += values[i] * d // x
        ans = res

        left = 0
        right = sum(values)

        for i in range(1, n):
            d = keys[i] - keys[i - 1]
            left += values[i - 1]
            right -= values[i - 1]

            res += left * d // x
            res -= right * d // x
            ans = min(ans, res)
        return ans


true, false, null = True, False, None
cases = [
    ([[2, 4], [6, 8]], 2, 4),
    ([[1, 5], [2, 3]], 1, 5),
    ([[1, 2], [3, 4]], 2, -1),
    ([[529, 529, 989], [989, 529, 345], [989, 805, 69]], 92, 25),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minOperations, cases)

if __name__ == '__main__':
    pass
