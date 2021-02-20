#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        count = [0] * 60
        for x in range(lowLimit, highLimit + 1):
            t = 0
            while x:
                t += x % 10
                x = x // 10
            count[t] += 1

        ans = max(count)
        return ans


cases = [
    (1, 10, 2),
    (5, 15, 2),
    (19, 28, 2)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().countBalls, cases)
