#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        left = [0] * n
        right = [0] * n

        left[0] = nums[0]
        for i in range(1, n):
            left[i] = max(left[i - 1], nums[i])

        right[-1] = nums[-1]
        for i in reversed(range(n - 1)):
            right[i] = min(right[i + 1], nums[i])

        # print(left, right)
        ans = 0
        for i in range(1, n - 1):
            if left[i - 1] < nums[i] < right[i + 1]:
                ans += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                ans += 1

        return ans


true, false, null = True, False, None
cases = [
    ([1, 2, 3, 4, 5, 7, 8, 9, 10], 14),
    ([3, 2, 1], 0),
    ([2, 4, 6, 4], 1),
    ([1, 2, 3], 2)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().sumOfBeauties, cases)

if __name__ == '__main__':
    pass
