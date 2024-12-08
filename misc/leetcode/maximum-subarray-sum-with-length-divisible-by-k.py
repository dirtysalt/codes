#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        acc = [0] * (n + 1)
        group = [[] for _ in range(k)]
        group[0].append(0)
        for i in range(n):
            acc[i + 1] = acc[i] + nums[i]
            group[(i + 1) % k].append(acc[i + 1])

        ans = -(1 << 63)
        for g in group:
            if not g: continue
            max_right = g[-1]
            for i in reversed(range(len(g) - 1)):
                res = max_right - g[i]
                ans = max(ans, res)
                max_right = max(max_right, g[i])
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 2], 1, 3),
    ([-1, -2, -3, -4, -5], 4, -10),
    ([-5, 1, 2, -3, 4], 2, 4),
]

aatest_helper.run_test_cases(Solution().maxSubarraySum, cases)

if __name__ == '__main__':
    pass
