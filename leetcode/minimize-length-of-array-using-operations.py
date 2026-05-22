#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        M = min(nums)
        cnt = 0
        for x in nums:
            if x == M:
                cnt += 1
            if x % M != 0:
                return 1
        return (cnt + 1) // 2


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 4, 3, 1], 1),
    ([5, 5, 5, 10, 5], 2),
    ([2, 3, 4], 1),
    ([3, 3, 1], 1),
    ([5, 2, 2, 2, 9, 10], 1)
]

aatest_helper.run_test_cases(Solution().minimumArrayLength, cases)

if __name__ == '__main__':
    pass
