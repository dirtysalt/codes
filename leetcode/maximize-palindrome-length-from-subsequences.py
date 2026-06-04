#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        w = word1 + word2
        n = len(w)
        dp = [[-1] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][i] = 1

        for sz in range(2, n + 1):
            for i in range(n - sz + 1):
                j = i + sz - 1
                seq = max(dp[i + 2][j + 1], dp[i + 1][j])
                base = dp[i + 2][j] if (i + 2) <= j else 0
                if w[i] == w[j] and base >= 0:
                    seq = max(seq, base + 2)
                dp[i + 1][j + 1] = seq

        last = [-1] * 26
        for i in range(len(word2)):
            c = ord(word2[i]) - ord('a')
            last[c] = i + len(word1)

        ans = 0
        for i in range(len(word1)):
            c = ord(word1[i]) - ord('a')
            p = last[c]
            if p == -1: continue
            d = dp[i + 2][p] if (i + 2) <= p else 0
            ans = max(ans, d + 2)
        return ans


cases = [
    ("cacb", "cbba", 5),
    ("aa", "bb", 0),
    ("ab", "ab", 3),
    ("eeeecd", "eabfbeeb", 7),
    ("afaaadacb", "ca", 6),
    ("aazzlizfmn", "nppqb", 2)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().longestPalindrome, cases)
