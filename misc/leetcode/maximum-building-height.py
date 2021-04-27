#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        if not restrictions: return n - 1
        restrictions.append((1, 0))
        restrictions.sort(key=lambda x: x[0])

        for i in range(1, len(restrictions)):
            (a, ha) = restrictions[i - 1]
            (b, hb) = restrictions[i]
            d = (b - a)
            if hb > (ha + d):
                restrictions[i] = (b, ha + d)

        for i in reversed(range(len(restrictions) - 1)):
            (a, ha) = restrictions[i]
            (b, hb) = restrictions[i + 1]
            d = (b - a)
            if ha > (hb + d):
                restrictions[i] = (a, hb + d)

        print(restrictions)

        ans = 0
        for i in range(1, len(restrictions)):
            (a, ha) = restrictions[i - 1]
            (b, hb) = restrictions[i]
            d = b - a
            x = (hb - ha + d) // 2
            maxh = ha + x
            # print('({}, {}) & ({}, {}) = {}'.format(a, ha, b, hb, maxh))
            ans = max(ans, maxh)

        ans = max(ans, n - restrictions[-1][0] + restrictions[-1][1])
        return ans


cases = [
    (5, [[2, 1], [4, 1]], 2),
    (6, [], 5),
    (10, [[5, 3], [2, 5], [7, 4], [10, 3]], 5),
    (100,
     [[68, 29], [89, 27], [66, 26], [34, 9], [53, 23], [93, 24], [70, 12], [25, 24], [5, 4], [94, 41], [51, 42],
      [6, 39], [55, 21], [69, 9], [39, 50], [99, 42], [77, 24], [81, 46], [90, 43], [27, 14], [31, 5], [67, 37],
      [82, 10], [26, 47], [84, 34], [37, 30], [83, 39], [21, 39], [49, 39], [13, 48], [12, 34], [57, 0], [7, 43],
      [17, 6], [23, 0], [86, 30], [47, 30], [61, 19], [30, 49], [95, 42], [3, 31], [33, 36], [11, 45], [75, 39],
      [85, 46], [29, 33], [2, 9], [22, 17], [65, 42], [96, 0], [35, 46], [88, 47], [74, 0], [73, 47], [41, 45],
      [15, 21], [97, 0], [64, 0], [40, 21], [76, 2], [54, 3], [24, 33], [45, 24], [16, 23], [91, 14], [43, 35], [79, 6],
      [46, 30], [71, 3], [9, 39], [50, 21], [48, 45], [63, 42], [58, 3], [10, 26], [4, 6], [52, 19], [32, 39], [87, 50],
      [8, 48], [19, 25], [92, 1], [28, 21], [59, 31], [72, 24], [78, 9], [100, 8], [60, 20], [42, 16], [38, 8],
      [62, 31], [36, 22], [44, 27], [14, 45], [18, 3], [98, 0], [20, 1], [56, 24], [80, 3]], 13)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxBuilding, cases)

if __name__ == '__main__':
    pass
