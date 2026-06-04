#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        from collections import Counter
        cnt = Counter()
        for x in nums:
            cnt[x] += 1
        keys = list(cnt.keys())
        keys.sort()
        print(keys)
        n = len(keys)
        dp = [0] * n
        for i in range(n):
            res = 0
            p = cnt[keys[i]] * keys[i]
            for k in range(1, 3 + 1):
                j = i - k
                if j < 0 or (keys[i] - keys[j]) == 1:
                    continue
                res = max(res, dp[j])
            dp[i] = res + p

        print(dp)
        ans = max(dp)
        return ans


cases = [
    ([10, 8, 4, 2, 1, 3, 4, 8, 2, 9, 10, 4, 8, 5, 9, 1, 5, 1, 6, 8, 1, 1, 6, 7, 8, 9, 1, 7, 6, 8, 4, 5, 4, 1, 5,
      9, 8, 6, 10, 6, 4, 3, 8, 4, 10, 8, 8, 10, 6, 4, 4, 4, 9, 6, 9, 10, 7, 1, 5, 3, 4, 4, 8, 1, 1, 2, 1, 4, 1, 1,
      4, 9, 4, 7, 1, 5, 1, 10, 3, 5, 10, 3, 10, 2, 1, 10, 4, 1, 1, 4, 1, 2, 10, 9, 7, 10, 1, 2, 7, 5], 338),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().deleteAndEarn, cases)
