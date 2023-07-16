#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        n = len(word)
        F = set(forbidden)
        dp = [0] * (n + 1)
        for i in reversed(range(n)):
            max_sz = min(10, n - i, dp[i + 1] + 1)
            hit = False
            for sz in range(1, max_sz + 1):
                sub = word[i: i + sz]
                if sub in F:
                    hit = True
                    break
                dp[i] = sz
            if not hit:
                dp[i] = min(n - i, dp[i + 1] + 1)

        return max(dp)


true, false, null = True, False, None
import aatest_helper

cases = [
    ("cbaaaabc", ["aaa", "cb"], 4),
    ("leetcode", ["de", "le", "e"], 4),
]

aatest_helper.run_test_cases(Solution().longestValidSubstring, cases)

if __name__ == '__main__':
    pass
