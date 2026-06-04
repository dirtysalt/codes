#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.copy()
        nums.sort()
        pos = n // 2

        ans = 0
        ans += abs(k - nums[pos])
        j = pos - 1
        while j >= 0 and nums[j] > k:
            ans += nums[j] - k
            j -= 1
        j = pos + 1
        while j < n and nums[j] < k:
            ans += k - nums[j]
            j += 1

        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([2, 5, 6, 8, 5], 4, 2),
    ([2, 5, 6, 8, 5], 7, 3),
    ([1, 2, 3, 4, 5, 6], 4, 0),
]

aatest_helper.run_test_cases(Solution().minOperationsToMakeMedianK, cases)

if __name__ == '__main__':
    pass
