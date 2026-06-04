#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def clumsy(self, N: int) -> int:
        tmp = []

        k = 1
        p = N
        for v in reversed(range(1, N)):
            if k == 0:
                tmp.append(p)
                p = v
            elif k == 1:
                p *= v
            elif k == 2:
                p = p // v
            elif k == 3:
                tmp.append(p)
                p = v
            k = (k + 1) % 4

        tmp.append(p)
        ans = tmp[0]
        sign = 1
        for i in range(1, len(tmp)):
            ans += sign * tmp[i]
            sign *= -1
        return ans


import aatest_helper

cases = [
    (10, 12),
    (4, 7),
    # (10000, aatest_helper.ANYTHING)
]

aatest_helper.run_test_cases(Solution().clumsy, cases)
