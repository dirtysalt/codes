#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        neg_inf = -(1 << 30)
        dp = {}

        def f(ab, x):
            # max delta
            if x >= len(stoneValue):
                return 0

            if (ab, x) in dp:
                return dp[(ab, x)]

            v = 0
            ans = neg_inf
            for i in range(3):
                if (i + x) >= len(stoneValue):
                    break

                v += stoneValue[i + x]
                res = f(1 - ab, i + x + 1)
                ans = max(ans, v - res)

            dp[(ab, x)] = ans
            return ans

        ans = f(0, 0)
        # print(dp, ans)
        if ans > 0:
            ans = 'Alice'
        elif ans < 0:
            ans = 'Bob'
        else:
            ans = 'Tie'
        return ans


cases = [
    ([1, 2, 3, 7], 'Bob')
]
import aatest_helper

aatest_helper.run_test_cases(Solution().stoneGameIII, cases)
