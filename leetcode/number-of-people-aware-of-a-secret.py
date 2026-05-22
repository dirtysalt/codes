#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [0] * n
        dp[0] = 1
        MOD = 10 ** 9 + 7
        for i in range(n):
            x = dp[i]
            for j in range(delay, forget):
                if (i + j) >= n: break
                dp[i + j] += x
        ans = sum(dp[-forget:]) % MOD
        return ans


true, false, null = True, False, None
cases = [
    (6, 2, 4, 5),
    (4, 1, 3, 6),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().peopleAwareOfSecret, cases)

if __name__ == '__main__':
    pass
