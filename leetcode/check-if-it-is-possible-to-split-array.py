#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        n = len(nums)
        if n <= 2: return True
        for i in range(n):
            val = nums[i] + (nums[i + 1] if (i + 1) < n else 0)
            if val >= m:
                return True
        return False


true, false, null = True, False, None
import aatest_helper

cases = [
    ([2, 2, 1], 4, true),
    ([2, 1, 3], 5, false),
    ([2, 3, 3, 2, 3], 6, true),
]

aatest_helper.run_test_cases(Solution().canSplitArray, cases)

if __name__ == '__main__':
    pass
