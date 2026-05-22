#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        n = len(nextVisit)
        acc = [0] * (n + 1)
        cyc = [0] * n

        MOD = 10 ** 9 + 7

        for i in range(n):
            back = nextVisit[i]
            if back == i:
                cyc[i] = 1
            else:
                cyc[i] = (acc[i] - acc[back]) + (i - back + 1)
                cyc[i] %= MOD
            acc[i + 1] = acc[i] + cyc[i]
            acc[i + 1] %= MOD

        # print(cyc)

        ans = 0
        for i in range(n - 1):
            # how many steps from i to i+1
            ans += cyc[i] + 1
            ans %= MOD

        return ans


true, false, null = True, False, None
cases = [
    ([0, 0], 2),
    ([0, 0, 2], 6),
    ([0, 1, 2, 0], 6)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().firstDayBeenInAllRooms, cases)

if __name__ == '__main__':
    pass
