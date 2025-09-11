#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        left = [[0] * (n + 1) for _ in range(n)]
        right = [[0] * (n + 1) for _ in range(n)]

        # left[i][j] means how many elements (<= ith) are less than j.
        for j in range(1, n + 1):
            last = 0
            for i in range(n):
                if nums[i] < j:
                    last += 1
                left[i][j] = last

        # right[i][j] means how many elements (>= ith) are greater than j
        for j in range(1, n + 1):
            last = 0
            for i in reversed(range(n)):
                if nums[i] > j:
                    last += 1
                right[i][j] = last

        ans = 0
        for j in range(1, n):
            for k in range(j + 1, n - 1):
                if nums[k] < nums[j]:
                    # nums[i] < nums[k]
                    a = left[j - 1][nums[k]]
                    # nums[j] < nums[l]
                    b = right[k + 1][nums[j]]
                    ans += a * b
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 3, 5, 2, 4], 1),
    ([1, 3, 2, 4, 5], 2),
    ([1, 2, 3, 4], 0),
]

aatest_helper.run_test_cases(Solution().countQuadruplets, cases)

if __name__ == '__main__':
    pass
