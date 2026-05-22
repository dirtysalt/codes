#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:

        s = sum(A)
        n = len(A)
        from collections import defaultdict
        dp = defaultdict(int)
        dp[0] = 1

        for k, x in enumerate(A):
            for y, c in list(dp.items()):
                # 这里直接做位移就好了
                # c2 = 0
                # for i in range(n - 1):
                #     if (c & (1 << i)) == 0:
                #         continue
                #
                #     c2 |= (1 << (i + 1))
                #     if (x + y) * (n - i - 1) == (s - x - y) * (i + 1):
                #         return True
                #
                # if c2 != 0:
                #     dp[x + y] |= c2
                dp[x + y] |= (c << 1)

        # 最后我们枚举切分的长度就好
        for k in range(1, n - 1):
            # x / k == (s - x) / (n - k)
            # x = sk / n
            if (s * k) % n == 0:
                x = s * k // n
                if dp[x] & (1 << k):
                    return True

        return False


cases = [
    ([6, 8, 18, 3, 1], False),
    ([1, 2, 3, 4, 5, 6, 7, 8], True),
    ([83, 60, 51, 90, 67, 62, 17, 56, 42, 11, 80, 8], True)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().splitArraySameAverage, cases)
