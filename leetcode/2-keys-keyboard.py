#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minSteps(self, n: int) -> int:
        from collections import defaultdict
        factors = defaultdict(list)
        for i in range(1, n + 1):
            factors[i].append(1)
            for j in range(2, i + 1):
                if j * j > i: break
                if i % j == 0:
                    factors[i].append(j)
                    factors[i].append(i // j)

        import functools
        @functools.lru_cache(maxsize=None)
        def fun(x):
            if x == 1: return 0
            ans = 10000
            for f in factors[x]:
                cost = x // f + fun(f)
                ans = min(ans, cost)
            return ans

        ans = fun(n)
        return ans


class Solution2:
    def minSteps(self, n: int) -> int:
        import functools
        @functools.lru_cache(maxsize=None)
        def fun(x):
            if x == 1: return 0
            ans = 10000
            for f in range(1, x):
                if x % f != 0: continue
                cost = x // f + fun(f)
                ans = min(ans, cost)
            return ans

        ans = fun(n)
        return ans


cases = [
    (1, 0),
    (3, 3),
    (18, 8)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minSteps, cases)
