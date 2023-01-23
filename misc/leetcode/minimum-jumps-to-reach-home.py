#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, X: int) -> int:
        forbidden = set(forbidden)
        visited = set()

        import heapq
        hp = []
        hp.append((0, 0, 1))

        while hp:
            x, c, d = heapq.heappop(hp)
            # print(x)
            if x == X:
                return c

            y = x + a
            # 这个上限有点不太好确定!!
            if y < 4000:
                if y not in forbidden and y not in visited:
                    visited.add(y)
                    heapq.heappush(hp, (y, c + 1, 1))

            if d == 1 and x >= b:
                y = x - b
                if y not in forbidden and y not in visited:
                    visited.add(y)
                    heapq.heappush(hp, (y, c + 1, 0))
        return -1


cases = [
    ([14, 4, 18, 1, 15], 3, 15, 9, 3),
    ([8, 3, 16, 6, 12, 20], 15, 13, 11, -1),
    ([1, 6, 2, 14, 5, 17, 4], 16, 9, 7, 2),
    ([162, 118, 178, 152, 167, 100, 40, 74, 199, 186, 26, 73, 200, 127, 30, 124, 193, 84, 184, 36, 103, 149, 153, 9, 54,
      154, 133, 95, 45, 198, 79, 157, 64, 122, 59, 71, 48, 177, 82, 35, 14, 176, 16, 108, 111, 6, 168, 31, 134, 164,
      136, 72, 98], 29, 98, 80, 121),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minimumJumps, cases)
