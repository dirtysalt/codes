#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10 ** 9 + 7

        import functools
        @functools.cache
        def dfs(i, x):
            if i == n:
                return 1
            ans = 0
            for z in range(max(nums[i] - nums[i - 1], 0) + x, nums[i] + 1):
                ans += dfs(i + 1, z)
            return ans

        ans = 0
        for x in range(0, nums[0] + 1):
            ans += dfs(1, x)
        return ans % MOD


true, false, null = True, False, None
import aatest_helper

cases = [
    ([2, 3, 2], 4),
    ([5, 5, 5, 5], 126),
]

aatest_helper.run_test_cases(Solution().countOfPairs, cases)

if __name__ == '__main__':
    pass
