#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def deleteString(self, s: str) -> int:
        n = len(s)
        dp = [-1] * (n + 1)
        dp[0] = 0

        for i in range(n):
            # assume s[:i] has been cut with times dp[i]
            if dp[i] == -1: continue

            for sz in range(1, (n - i) // 2 + 1):
                if s[i:i + sz] == s[i + sz:i + sz * 2]:
                    j = i + sz
                    assert (j < n)
                    dp[j] = max(dp[j], dp[i] + 1)

        # the last cut must be total cut.
        ans = 0
        for i in range(n):
            if dp[i] != -1:
                ans = max(ans, dp[i] + 1)
        return ans


true, false, null = True, False, None
cases = [
    ("abcabcdabc", 2),
    ("aaabaab", 4),
    ("aaaaa", 5)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().deleteString, cases)

if __name__ == '__main__':
    pass
