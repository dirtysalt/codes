#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        pos = [n] * (n + 1)
        for i in reversed(range(n)):
            pos[i] = i if s[i] == '0' else pos[i + 1]

        ans = 0
        for l in range(n):
            zero = 0
            r0 = pos[l]
            # [l..r0][r0+1..r1)
            # s[r0/r1] == '0'
            ans += (r0 - l)

            while r0 < n:
                zero += 1
                if zero * zero > (n - l): break
                r1 = pos[r0 + 1]
                a = (r0 - l + 1) - zero
                b = max(zero * zero - a, 0)
                if b > (n - r0): break
                r = max(r1 - r0 - b, 0)
                ans += r
                r0 = r1
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ("011", 5),
    ("00011", 5),
    ("101101", 16)
]
cases += aatest_helper.read_cases_from_file('tmp.in', 2)

aatest_helper.run_test_cases(Solution().numberOfSubstrings, cases)

if __name__ == '__main__':
    pass
