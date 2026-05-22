#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int],
                         experience: List[int]) -> int:
        a, b = initialEnergy, initialExperience
        ans = 0

        for x, y in zip(energy, experience):
            if a <= x:
                ans += x + 1 - a
                a = x + 1
            if b <= y:
                ans += y + 1 - b
                b = y + 1
            a -= x
            b += y
        return ans


true, false, null = True, False, None
cases = [
    (5, 3, [1, 4, 3, 2], [2, 6, 3, 1], 8),
    (2, 4, [1], [3], 0),
    (5, 3, [1, 4, 3, 2], [2, 6, 3, 1], 8),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minNumberOfHours, cases)

if __name__ == '__main__':
    pass
