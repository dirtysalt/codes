#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        pos = []

        seat = 0
        for i in range(len(corridor)):
            if corridor[i] == 'S':
                seat += 1
                pos.append(i)
        if seat == 0 or seat % 2 != 0:
            return 0

        # print(pos)
        MOD = 10 ** 9 + 7
        ans = 1
        for i in range(2, len(pos), 2):
            dist = pos[i] - pos[i - 1]
            ans *= dist
        return ans % MOD


true, false, null = True, False, None
cases = [
    ("SSPPSPS", 3),
    ("PPSPSP", 1),
    ("S", 0),
    ("P", 0),
    ("SPPSSSSPPS", 1)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().numberOfWays, cases)

if __name__ == '__main__':
    pass
