#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        tmp = [a, b, c]
        ans = 0
        while True:
            tmp.sort()
            x, y = tmp[-2], tmp[-1]
            if x > 0 and y > 0:
                tmp[-2] -= 1
                tmp[-1] -= 1
            else:
                break
            ans += 1
        return ans


cases = [
    (2, 4, 6, 6),
    (4, 4, 6, 7),
    (1, 8, 8, 8)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maximumScore, cases)
