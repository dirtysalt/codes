#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:

        n = len(s)
        dp = [[0] * 26 for _ in range(2)]
        now = 0

        for i in range(n):
            c = ord(s[i]) - ord('a')
            for j in range(26):
                if abs(c - j) <= k:
                    dp[1 - now][c] = max(dp[1 - now][c], dp[now][j] + 1)
            for j in range(26):
                dp[1 - now][j] = max(dp[1 - now][j], dp[now][j])
            now = 1 - now

        return max(dp[now])


true, false, null = True, False, None
cases = [
    ("acfgbd", 2, 4),
    ("abcd", 3, 4),
    ("eduktdb", 15, 5),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().longestIdealString, cases)

if __name__ == '__main__':
    pass
