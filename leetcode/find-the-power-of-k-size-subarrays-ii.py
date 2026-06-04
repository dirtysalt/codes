#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def resultsArray(self, nums: List[int], K: int) -> List[int]:
        n = len(nums)

        j = 0
        end = [0] * n
        for i in range(1, n):
            if nums[i] - nums[i - 1] != 1:
                for k in range(j, i):
                    end[k] = i - 1
                j = i

        for k in range(j, n):
            end[k] = n - 1

        ans = []
        for i in range(n - K + 1):
            e = nums[end[i]]
            value = nums[i] + K - 1
            if value > e:
                value = -1
            ans.append(value)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 2, 3, 4, 3, 2, 5], 3, [3, 4, -1, -1, -1]),
    ([2, 2, 2, 2, 2, ], 4, [-1, -1]),
    ([3, 2, 3, 2, 3, 2], 2, [-1, 3, -1, 3, -1]),
]

aatest_helper.run_test_cases(Solution().resultsArray, cases)

if __name__ == '__main__':
    pass
