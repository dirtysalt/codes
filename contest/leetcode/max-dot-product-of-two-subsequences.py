#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        ninf = -(1 << 30)
        dp = [[ninf] * (m + 1) for _ in range(n + 1)]
        dp2 = [[ninf] * (m + 1) for _ in range(n + 1)]
        # dp[i][j]是考慮到i,j的最大值, 可以不適用任何點對
        # dp2[i][j]在dp上擴展， 但是必須是使用至少一次點對
        for i in range(n + 1):
            dp[i][0] = 0
        for i in range(m + 1):
            dp[0][i] = 0

        ans = ninf
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + max(0, nums1[i - 1] * nums2[j - 1]))
                dp2[i][j] = max(dp2[i - 1][j], dp2[i][j - 1], dp[i - 1][j - 1] + nums1[i - 1] * nums2[j - 1])
                ans = max(ans, dp2[i][j])
        # print(dp, dp2)
        return ans


cases = [
    ([2, 1, -2, 5], [3, 0, -6], 18),
    ([3, -2], [2, -6, 7], 21),
    ([-1, -1], [1, 1], -1),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxDotProduct, cases)
