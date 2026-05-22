#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        # dp[i][sz]: starts with i, and size is sz
        dp = [[0] * (n+1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = dp[i][1] = 1

        for sz in range(2, n + 1):
            for i in range(n - sz + 1):
                j = i + sz - 1
                if s[i] == s[j] and dp[i + 1][sz - 2]:
                    dp[i][sz] = 1

        for i in range(1, n - 1):
            for j in range(i + 1, n):
                # [0.. i], [i..j], [j..]
                if dp[0][i] and dp[i][j - i] and dp[j][n - j]:
                    return True
        return False


cases = [
    ("abcbdd", True,),
    ("bcbddxy", False),
    ("bbab", True),
    ("aaa", True)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().checkPartitioning, cases)
