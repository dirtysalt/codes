#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        from collections import Counter
        cnt = Counter()

        def use_size(sz):
            # print('use sz', sz)
            res = 0
            mask = [0] * 26
            j = 0
            k = 0
            for i in range(len(s)):
                c = s[i]
                x = ord(c) - ord('a')
                mask[x] += 1
                if mask[x] == 1:
                    k += 1

                while j <= i and (k > maxLetters or (i - j + 1) > sz):
                    c = s[j]
                    x = ord(c) - ord('a')
                    mask[x] -= 1
                    if mask[x] == 0:
                        k -= 1
                    j += 1

                if (i - j + 1) == sz:
                    subs = s[j:i + 1]
                    cnt[subs] += 1
                    # print(subs, sz, cnt[subs])
                    res = max(res, cnt[subs])
            return res

        ans = 0
        for sz in range(minSize, maxSize + 1):
            r = use_size(sz)
            ans = max(r, ans)
        return ans


cases = [
    ("aababcaab", 2, 3, 4, 2),
    ("aababcaab", 2, 2, 3, 3)
]
import aatest_helper

aatest_helper.run_test_cases(Solution().maxFreq, cases)
