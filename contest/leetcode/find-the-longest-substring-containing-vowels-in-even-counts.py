#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        n = len(s)
        mapping = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        inf = 1 << 30
        dp = [inf] * 32
        dp[0] = -1

        res = 0
        ans = 0
        for i in range(n):
            c = s[i]
            v = mapping.get(c)
            if v is not None:
                res ^= (1 << v)
            if dp[res] != inf:
                ans = max(ans, i - dp[res])
            else:
                dp[res] = i
        return ans


cases = [
    ("eleetminicoworoep", 13),
    ("leetcodeisgreat", 5),
    ("bcbcbc", 6)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().findTheLongestSubstring, cases)
