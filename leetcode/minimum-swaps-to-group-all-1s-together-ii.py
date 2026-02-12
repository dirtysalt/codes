#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        loop = nums + nums
        exp = sum(nums)
        zero = exp - sum(loop[:exp])
        ans = zero
        for i in range(exp, len(loop)):
            if loop[i] == 0:
                zero += 1
            if loop[i - exp] == 0:
                zero -= 1
            ans = min(ans, zero)
        return ans


true, false, null = True, False, None
cases = [
    ([0, 1, 0, 1, 1, 0, 0], 1),
    ([0, 1, 1, 1, 0, 0, 1, 1, 0], 2),
    ([1, 1, 0, 0, 1], 0),
    ([1, 1, 1, 0, 0, 1, 0, 1, 1, 0], 1),
    ([1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0], 7)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minSwaps, cases)

if __name__ == '__main__':
    pass
