#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n == 1: return 0
        if n % 2 == 0:
            n = n // 2
        return n


true, false, null = True, False, None
import aatest_helper

cases = [
    (4, 2),
    (3, 3),
    (6, 3),
    (8, 4),
]

aatest_helper.run_test_cases(Solution().numberOfCuts, cases)

if __name__ == '__main__':
    pass
