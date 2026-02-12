#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        remain = [0] * k
        ans = [0] * k
        for x in reversed(nums):
            remain2 = [0] * k
            for r in range(k):
                remain2[(r * x) % k] += remain[r]
            remain2[x % k] += 1
            for r in range(k):
                ans[r] += remain2[r]
            remain = remain2
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 2, 3, 4, 5], 3, [9, 2, 4]),
    ([1, 2, 4, 8, 16, 32], 4, [18, 1, 2, 0],),
    ([1, 1, 2, 1, 1], 2, [9, 6]),
]

aatest_helper.run_test_cases(Solution().resultArray, cases)

if __name__ == '__main__':
    pass
