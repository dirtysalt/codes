#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        from collections import Counter
        cnt = Counter()
        for d in deliciousness:
            cnt[d] += 1

        ans = 0
        for x in deliciousness:
            for i in range(22):
                y = (1 << i) - x
                res = cnt[y]
                if x == y:
                    res -= 1
                ans += res

        ans = ans // 2
        MOD = 10 ** 9 + 7
        ans = ans % MOD
        return ans


cases = [
    ([1, 3, 5, 7, 9], 4),
    ([1, 1, 1, 3, 3, 3, 7], 15),
    ([1, 1, 1], 3)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().countPairs, cases)
