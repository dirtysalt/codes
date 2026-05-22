#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        n = len(nums)
        INF = 1 << 30
        dp = [INF] * (n + 1)
        dp[0] = 0
        for i in range(n):
            # base on dp[i]
            # and ccheck [i..]
            from collections import Counter
            cnt = Counter()
            sz = 0
            for j in range(i, n):
                x = nums[j]
                cnt[x] += 1
                c = cnt[x]
                if c == 2:
                    sz += 2
                elif c > 2:
                    sz += 1
                dp[j + 1] = min(dp[i] + sz + k, dp[j + 1])
        return dp[n]


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 2, 1, 2, 1, 3, 3], 2, 8),
    ([1, 2, 1, 2, 1], 2, 6),
    ([1, 2, 1, 2, 1], 5, 10),
]

aatest_helper.run_test_cases(Solution().minCost, cases)

if __name__ == '__main__':
    pass
