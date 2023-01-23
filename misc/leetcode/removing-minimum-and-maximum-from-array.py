#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        m0 = min(nums)
        m1 = max(nums)
        i = nums.index(m0)
        j = nums.index(m1)
        n = len(nums)

        if i == j:
            return min(i + 1, n - i)
        if i > j:
            i, j = j, i

        a = max(i + 1, j + 1)
        b = max(n - i, n - j)
        c = i + 1 + n - j
        ans = min(a, b, c)
        return ans


true, false, null = True, False, None
cases = [
    ([2, 10, 7, 5, 4, 1, 8, 6], 5),
    ([0, -4, 19, 1, 8, -2, -3, 5], 3),
    ([101], 1)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minimumDeletions, cases)

if __name__ == '__main__':
    pass
