#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        from collections import Counter
        cnt = Counter()

        ans = 0
        mask = [0] * 26
        j = 0
        k = 0
        for i in range(len(s)):
            c = s[i]
            x = ord(c) - ord('a')
            mask[x] += 1
            if mask[x] == 1:
                k += 1

            while j <= i and (k > maxLetters or (i - j + 1) > maxSize):
                c = s[j]
                x = ord(c) - ord('a')
                mask[x] -= 1
                if mask[x] == 0:
                    k -= 1
                j += 1

            # j .. i is qualified.
            # ending with s[i]
            for kk in range(j, i + 1):
                if (i - kk + 1) < minSize:
                    break
                subs = s[kk:i + 1]
                cnt[subs] += 1
                ans = max(ans, cnt[subs])
        return ans


cases = [
    ("aababcaab", 2, 3, 4, 2),
    ("aababcaab", 2, 2, 3, 3),
    ("bbacbadadc", 2, 1, 1, 3),
]
import aatest_helper

aatest_helper.run_test_cases(Solution().maxFreq, cases)
