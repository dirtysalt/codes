#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1
        cnt.sort(reverse=True)

        dup = set()
        ans = 0
        for i in range(26):
            x = cnt[i]
            # at most 26 times.
            while x and x in dup:
                ans += 1
                x -= 1
            if x == 0: continue
            dup.add(x)

        return ans


cases = [
    ("aab", 0),
    ("aaabbbcc", 2),
    ("ceabaacb", 2),
    ("bbcebab", 2)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minDeletions, cases)
