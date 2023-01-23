#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        from collections import Counter
        c = Counter(nums)
        keys = sorted(list(c.keys()))

        K = k
        for k in keys:
            init = c[k]
            if init == 0:
                continue
            for k2 in range(k + 1, k + K):
                if c[k2] < init:
                    return False
                c[k2] -= init
        return True


cases = [
    ([3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11], 3, True),
    ([1, 2, 3, 4], 3, False)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().isPossibleDivide, cases)
