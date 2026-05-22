#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)

        def maxdist(s):
            dist = [1] * n

            for i in range(1, n):
                d = dist[i - 1]
                p = i - d - 1

                if p < 0:
                    # try small dist.
                    d -= 2
                    p += 2

                while s[i] != s[p]:
                    d -= 2
                    p += 2

                if s[i] == s[p]:
                    dist[i] = d + 2

                # don't need even length.
                # elif s[i] == s[i - 1]:
                #     dist[i] = 2

            for i in range(1, n):
                dist[i] = max(dist[i], dist[i - 1])

            return dist

        d1 = maxdist(s)
        d2 = maxdist(s[::-1])
        ans = 0
        for i in range(n - 1):
            a = d1[i]
            b = d2[n - 1 - (i + 1)]
            ans = max(ans, a * b)
        return ans


true, false, null = True, False, None
cases = [
    ("ababbb", 9),
    ("zaaaxbbby", 9),
    ("ggbswiymmlevedhkbdhntnhdbkhdevelmmyiwsbgg", 45),
    ('aaaaaa', 9),
    ('aaaaaaa', 9),
    ('aaaaaaaaa', 15),
    ('aaaaaaaa', 15),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxProduct, cases)

if __name__ == '__main__':
    pass
