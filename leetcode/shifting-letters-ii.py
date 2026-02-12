#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        def create(shifts):
            ev = []
            for (x, y, d) in shifts:
                if d == 0: d = -1
                ev.append((x, d))
                ev.append((y + 1, -d))
            ev.sort()
            return ev

        def merge(ev):
            x, d = ev[0]
            res = []
            for i in range(1, len(ev)):
                if ev[i][0] == x:
                    d += ev[i][1]
                else:
                    res.append((x, d))
                    x, d = ev[i]
            res.append((x, d))
            return res

        ev = create(shifts)
        ev = merge(ev)
        op = [0] * len(s)
        last, dd = 0, 0
        for (x, d) in ev:
            for i in range(last, x):
                op[i] += dd
            last = x
            dd += d
        ans = []
        for i in range(len(s)):
            c = ord(s[i]) - ord('a')
            c += op[i]
            c = c % 26
            ans.append(chr(c + ord('a')))
        return ''.join(ans)


true, false, null = True, False, None
cases = [
    ("abc", [[0, 1, 0], [1, 2, 1], [0, 2, 1]], "ace"),
    ("dztz", [[0, 0, 0], [1, 1, 1]], "catz"),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().shiftingLetters, cases)

if __name__ == '__main__':
    pass
