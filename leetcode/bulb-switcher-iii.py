#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        n = len(light)
        on = [0] * n
        right = 0
        left = -1

        ans = 0
        for x in light:
            x -= 1
            if x > right:
                right = x
            on[x] = 1
            while (left + 1) < n and on[left + 1] == 1:
                left += 1
            if left == right:
                ans += 1

        return ans


cases = [
    ([2, 1, 3, 5, 4], 3),
    ([3, 2, 4, 1, 5], 2)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().numTimesAllBlue, cases)
