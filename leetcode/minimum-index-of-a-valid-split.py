#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        from collections import Counter
        cnt = Counter(nums)
        left = Counter()

        for i in range(len(nums)):
            x = nums[i]
            cnt[x] -= 1
            left[x] += 1
            if left[x] * 2 > (i + 1) and cnt[x] * 2 > (len(nums) - i - 1):
                return i
        return -1


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 2, 2, 2], 2),
    ([2, 1, 3, 1, 1, 1, 7, 1, 2, 1], 4),
    ([3, 3, 3, 3, 7, 2, 2], -1),
    ([9, 5, 5, 1, 1, 1, 1, 8, 1], -1),
]

aatest_helper.run_test_cases(Solution().minimumIndex, cases)

if __name__ == '__main__':
    pass
