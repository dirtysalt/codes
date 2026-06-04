#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        req = {x[0] + 1: x[1] for x in requirements}
        m = max([x[1] for x in requirements])
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            for rev in range(m + 1):
                if i in req and rev != req[i]: continue
                res = 0
                for j in range(0, i):
                    # less than how many elements ? which is new rev.
                    if rev < j: break
                    res += dp[i - 1][rev - j]
                dp[i][rev] = res

        return dp[n][m] % MOD


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(n=3, requirements=[[2, 2], [0, 0]], res=2),
    aatest_helper.OrderedDict(n=3, requirements=[[2, 2], [1, 1], [0, 0]], res=1),
    aatest_helper.OrderedDict(n=2, requirements=[[0, 0], [1, 0]], res=1),
]

aatest_helper.run_test_cases(Solution().numberOfPermutations, cases)

if __name__ == '__main__':
    pass
