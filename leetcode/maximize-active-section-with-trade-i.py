#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        j = 0
        base = 0
        segs = []
        for i, c in enumerate(s):
            if c == '1':
                base += 1
            if s[i] != s[j]:
                segs.append((j, i - 1))
                j = i
        segs.append((j, len(s) - 1))
        # print(segs)

        ans = 0
        for i in range(len(segs)):
            a, b = segs[i]
            if s[a] == '1':
                if (i - 1) >= 0 and (i + 1) < len(segs):
                    sz = (segs[i - 1][1] - segs[i - 1][0] + 1) + (segs[i + 1][1] - segs[i + 1][0] + 1)
                    ans = max(ans, sz)

        return ans + base


true, false, null = True, False, None
import aatest_helper

cases = [
    ('01', 1),
    ('0100', 4),
    ('1000100', 7),
    ('01010', 4),
    ('101', 2),
]

aatest_helper.run_test_cases(Solution().maxActiveSectionsAfterTrade, cases)

if __name__ == '__main__':
    pass
