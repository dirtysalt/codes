#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        # dp[i] = dp[j+1] + .. + dp[n-1]  where nums[i] = nums[j].
        # acc[i] = acc[i] + acc[i+1]  + acc[n-1]
        n = len(nums)

        direct = {}
        for i in range(n):
            direct[nums[i]] = i

        last = [-1] * n
        visited = [0] * n
        for i in range(n):
            if visited[i]: continue
            j = i
            end = direct[nums[i]]
            while j < end:
                end = max(direct[nums[j]], end)
                j += 1
            last[i] = end
            for k in range(i, j + 1):
                visited[k] = 1

        MOD = 10 ** 9 + 7
        # print(last)
        dp = [0] * n
        acc = [0] * (n + 1)
        acc[-1] = 1
        for i in reversed(range(n)):
            p = last[i]
            if p == -1:
                dp[i] = 0
            else:
                dp[i] = acc[p + 1]
            acc[i] = (acc[i + 1] + dp[i]) % MOD
        return dp[0]


true, false, null = True, False, None
import aatest_helper

cases = [
    ([3, 4], 2),
    ([1, 2, 3, 4], 8),
    ([1, 1, 1, 1], 1),
    ([1, 2, 1, 3], 2),
    ([1, 5, 1, 5, 6], 2),
    ([2, 3, 2, 8, 8], 2),
]

aatest_helper.run_test_cases(Solution().numberOfGoodPartitions, cases)

if __name__ == '__main__':
    pass
