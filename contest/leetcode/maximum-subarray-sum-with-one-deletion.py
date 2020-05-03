#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = arr[0]
        dp[0][1] = 0

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], 0) + arr[i]
            dp[i][1] = max(dp[i-1][1] + arr[i], dp[i-1][0])

        ans = max((x[0] for x in dp))
        if n > 1:
            # 不能选择第一个去掉1个之后的结果，这是空数组
            ans = max(ans, max((x[1] for x in dp[1:])))
        return ans


cases = [
    ([1, -2, 0, 3], 4),
    ([1, -2, -2, 3], 3),
    ([-1, -1, -1, -1], -1)
]

import aatest_helper
aatest_helper.run_test_cases(Solution().maximumSum, cases)
