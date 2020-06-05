#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        n = len(tree)
        ts = [0] * n
        c = 0
        j = 0
        ans = 0
        for i in range(n):
            t = tree[i]
            ts[t] += 1
            if ts[t] == 1:
                c += 1

            while j <= i and c > 2:
                t = tree[j]
                ts[t] -= 1
                if ts[t] == 0:
                    c -= 1
                j += 1

            ans = max(ans, i - j + 1)
        return ans


cases = [
    ([1, 2, 1], 3),
    ([0, 1, 2, 2], 3),
    ([1, 2, 3, 2, 2], 4),
    ([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4], 5)
]
import aatest_helper

aatest_helper.run_test_cases(Solution().totalFruit, cases)
