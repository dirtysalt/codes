#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        import heapq

        buy = []
        sell = []
        ans = 0
        tt = 0
        for p, am, o in orders:
            tt += am
            if o == 0: #buy
                # find sell
                while sell and am:
                    (p2, am2) = heapq.heappop(sell)
                    # print('buy', am, am2, p2, p)
                    ok = False
                    if p2 <= p:
                        exe = min(am, am2)
                        am2 -= exe
                        am -= exe
                        ans += exe
                        ok = True
                    if am2:
                        heapq.heappush(sell, (p2, am2))
                    if not ok: break

                if am:
                    heapq.heappush(buy, (-p, am))

            elif o == 1: #sell
                # find buy
                while buy and am:
                    (p2, am2) = heapq.heappop(buy)
                    # print('sell', am, am2, p2, p)
                    p2 = -p2
                    ok = False
                    if p2 >= p:
                        exe = min(am, am2)
                        am2 -= exe
                        am -= exe
                        ans += exe
                        ok = True
                    if am2:
                        heapq.heappush(buy, (-p2, am2))
                    if not ok: break

                if am:
                    heapq.heappush(sell, (p, am))

        MOD = 10 ** 9 +7
        tt = tt - 2 * ans
        return tt % MOD

cases = [
    ( [[10,5,0],[15,2,1],[25,1,1],[30,4,0]], 6),
    ([[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]], 999999984),
]

import aatest_helper
aatest_helper.run_test_cases(Solution().getNumberOfBacklogOrders, cases)


if __name__ == '__main__':
    pass
