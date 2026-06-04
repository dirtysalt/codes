#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def numWays(self, s: str) -> int:
        MOD = 10 ** 9 + 7

        ps = []
        n = len(s)
        for i in range(n):
            if s[i] == '1':
                ps.append(i)
        if not ps:
            # C(n-1,2)
            ans = (n - 1) * (n - 2) // 2
            ans = ans % MOD
            return ans

        if len(ps) % 3 != 0: return 0

        avg = len(ps) // 3
        a = ps[avg - 1:avg + 1]
        b = ps[2 * avg - 1:2 * avg + 1]
        ans = (a[1] - a[0]) * (b[1] - b[0])
        ans = ans % MOD
        return ans


true, false, null = True, False, None
cases = [
    ("100100010100110", 12),
    ("0000", 3),
    ("1001", 0),
    ("10101", 4),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().numWays, cases)

if __name__ == '__main__':
    pass
