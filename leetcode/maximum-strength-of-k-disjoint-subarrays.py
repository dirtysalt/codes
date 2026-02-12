#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        INF = (1 << 63)
        dp = [[-INF] * (k + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 0

        # dp[i-1][k] =
        #  -> dp[i][k] + r1
        #  -> dp[i][k+1] + r2
        for i in range(1, n + 1):
            for j in range(0, k + 1):
                if dp[i - 1][j] == -INF: continue

                if j != 0:
                    r1 = nums[i - 1] * (k - j + 1)
                    if j % 2 == 0:
                        r1 = -r1
                    dp[i][j] = max(dp[i][j], dp[i - 1][j] + r1)

                if (j + 1) <= k:
                    r2 = nums[i - 1] * (k - j)
                    if (j + 1) % 2 == 0:
                        r2 = -r2
                    dp[i][j + 1] = max(dp[i][j + 1], dp[i - 1][j] + r2)

        ans = -INF
        for i in range(1, n + 1):
            ans = max(ans, dp[i][k])
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(nums=[1], k=1, res=1),
    aatest_helper.OrderedDict(nums=[1, 2, 3, -1, 2], k=3, res=22),
    aatest_helper.OrderedDict(nums=[12, -2, -2, -2, -2], k=5, res=64),
    aatest_helper.OrderedDict(nums=[-1, -2, -3], k=1, res=-1),
    ([-99, 85], 1, 85),
]

aatest_helper.run_test_cases(Solution().maximumStrength, cases)

if __name__ == '__main__':
    pass
