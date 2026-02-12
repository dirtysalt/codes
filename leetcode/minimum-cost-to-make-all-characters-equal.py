#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        ss = [int(x) for x in s]

        import functools
        @functools.cache
        def search(i, d, exp):
            if i == -1 or i == n: return 0
            x = ss[i]
            if x == exp:
                return search(i + d, d, exp)
            else:
                r = search(i + d, d, 1 - exp)
                if d == -1:
                    c = i + 1
                else:
                    c = n - i
                return r + c

        INF = 10 ** 10
        ans = INF
        for i in range(-1, n):
            r0 = search(i, -1, 0)
            r1 = search(i + 1, 1, 0)
            ans = min(ans, r0 + r1)

        for i in range(-1, n):
            r0 = search(i, -1, 1)
            r1 = search(i + 1, 1, 1)
            ans = min(ans, r0 + r1)

        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ("0011", 2),
    ("010101", 9),
]

aatest_helper.run_test_cases(Solution().minimumCost, cases)

if __name__ == '__main__':
    pass
