#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        ds = []

        m = 0
        while targetSeconds >= 0 and m < 100:
            if targetSeconds < 100:
                ds.append((m, targetSeconds))
            m += 1
            targetSeconds -= 60

        def cost(m, s):
            tmp = [m // 10, m % 10, s // 10, s % 10]
            while tmp and tmp[0] == 0:
                tmp.pop(0)

            c = 0
            p = startAt
            for x in tmp:
                if p != x:
                    c += moveCost
                c += pushCost
                p = x
            return c

        ans = 1 << 30
        for m, s in ds:
            c = cost(m, s)
            ans = min(ans, c)
        return ans


true, false, null = True, False, None
cases = [
    (7, 220, 479, 6000, 2576)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minCostSetTime, cases)

if __name__ == '__main__':
    pass
