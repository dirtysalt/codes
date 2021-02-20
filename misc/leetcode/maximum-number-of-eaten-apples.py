#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        import heapq

        hp = []
        ans = 0
        for i in range(len(apples)):
            a = apples[i]
            if a:
                d = days[i]
                exp = d + i
                heapq.heappush(hp, (exp, a))

            while hp:
                (exp, a) = heapq.heappop(hp)
                if i >= exp: continue
                a -= 1
                ans += 1
                if a:
                    heapq.heappush(hp, (exp, a))
                break

        i = len(apples)
        while hp:
            (exp, a) = heapq.heappop(hp)
            if i >= exp: continue
            eat = min((exp - i), a)
            i += eat
            ans += eat
        return ans


import aatest_helper

cases = [
    ([1, 2, 3, 5, 2], [3, 2, 1, 4, 2], 7),
    ([3, 0, 0, 0, 0, 2], [3, 0, 0, 0, 0, 2], 5),
]

aatest_helper.run_test_cases(Solution().eatenApples, cases)
