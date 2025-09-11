#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def largestVariance(self, s: str) -> int:
        s = [ord(c) - ord('a') for c in s]
        ss = set(s)

        def test(s, c1, c2):
            t = 0
            res = 0
            x2 = 1
            for i in range(len(s)):
                c = s[i]
                if c == c1:
                    t += 1
                    res = max(res, t - x2)
                elif c == c2:
                    t -= 1
                    x2 = 0
                    if t < 0:
                        t = 0
                        x2 = 1
            return res

        ans = 0
        for c1 in ss:
            for c2 in ss:
                if c1 == c2: continue
                t = test(s, c1, c2)
                ans = max(ans, t)
        return ans


true, false, null = True, False, None
cases = [
    ("aababbb", 3),
    ("abcde", 0),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().largestVariance, cases)

if __name__ == '__main__':
    pass
