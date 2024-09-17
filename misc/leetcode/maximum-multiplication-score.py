#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        n = len(b)
        from math import inf
        dp = [0] * (n + 1)
        for k in reversed(range(4)):
            dp2 = [-inf] * (n + 1)
            for i in reversed(range(n)):
                dp2[i] = max(dp2[i + 1], a[k] * b[i] + dp[i + 1])
            dp = dp2
            # print(dp)
        return dp[0]


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(a=[3, 2, 5, 6], b=[2, -6, 4, -5, -3, 2, -7], res=26),
    aatest_helper.OrderedDict(a=[-1, 4, 5, -2], b=[-5, -1, -3, -2, -4], res=-1)
]

aatest_helper.run_test_cases(Solution().maxScore, cases)

if __name__ == '__main__':
    pass
