#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        from collections import defaultdict
        dp = defaultdict(int)
        ans = 0

        for x in arr:
            exp = x - difference
            sz = dp[exp] + 1
            dp[x] = max(dp[x], sz)
            ans = max(ans, sz)

        return ans


cases = [
    ([1, 5, 7, 8, 5, 3, 4, 2, 1], -2, 4),
    ([1, 3, 5, 7], 1, 1),
    ([1, 2, 3, 4], 1, 4)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().longestSubsequence, cases)
