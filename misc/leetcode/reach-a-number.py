#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)

        # (n + 1) * n // 2 <= target
        n = int(((1 + 8 * target) ** 0.5 - 1) // 2)
        while (n + 1) * n // 2 < target:
            n += 1

        if target % 2 == 0:
            while n % 4 != 0 and n % 4 != 3:
                n += 1
        else:
            while n % 4 != 1 and n % 4 != 2:
                n += 1
        return n


cases = [
    (2, 3),
    (3, 2),
    (8, 4),
]
import aatest_helper

aatest_helper.run_test_cases(Solution().reachNumber, cases)
