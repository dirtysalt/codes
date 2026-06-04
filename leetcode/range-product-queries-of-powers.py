#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = []
        MOD = 10 ** 9 + 7

        powers = []
        for i in range(32):
            if (n >> i) & 0x1:
                powers.append(1 << i)

        for p, q in queries:
            t = 1
            for i in range(p, q + 1):
                t *= powers[i]
            ans.append(t % MOD)

        return ans


true, false, null = True, False, None
cases = [
    (15, [[0, 1], [2, 2], [0, 3]], [2, 4, 64]),
    (2, [[0, 0]], [2]),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().productQueries, cases)

if __name__ == '__main__':
    pass
