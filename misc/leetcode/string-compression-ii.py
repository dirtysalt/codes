#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

        dp = {}
        inf = 1 << 30

        def f(i, k, last_c, last_occ):
            if i == len(s):
                if last_occ in (0, 1):
                    return last_occ
                else:
                    return 1 + len(str(last_occ))

            key = (i, k, last_c, last_occ)
            if key in dp:
                return dp[key]

            ans = inf
            if k > 0:
                t0 = f(i + 1, k - 1, last_c, last_occ)
                ans = min(ans, t0)

            if s[i] == last_c:
                t1 = f(i + 1, k, last_c, last_occ + 1)
            else:
                if last_occ in (0, 1):
                    dt = last_occ
                else:
                    dt = 1 + len(str(last_occ))

                t1 = f(i + 1, k, s[i], 1) + dt

            ans = min(ans, t1)
            dp[key] = ans
            return ans

        ans = f(0, k, None, 0)
        return ans


cases = [
    # ("aaabcccd", 2, 4),
    # ("aabbaa", 2, 2),
    # ("aaaaaaaaaaa", 0, 3),
    ("abcdefghijklmnopqrstuvwxyz", 16, 11)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().getLengthOfOptimalCompression, cases)
