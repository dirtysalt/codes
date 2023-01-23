#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        ss = [tuple(x) for x in stockPrices]
        ss.sort()
        n = len(ss)
        if n == 1: return 0
        if n == 2: return 1

        dx, dy = ss[1][0] - ss[0][0], ss[1][1] - ss[0][1]
        ans = 1
        for i in range(2, n):
            a, b = ss[i][0] - ss[i - 1][0], ss[i][1] - ss[i - 1][1]
            if dy * a == dx * b:
                continue
            else:
                ans += 1
                dx, dy = a, b
        return ans


true, false, null = True, False, None
cases = [
    ([[1, 7], [2, 6], [3, 5], [4, 4], [5, 4], [6, 3], [7, 2], [8, 1]], 3),
    ([[3, 4], [1, 2], [7, 8], [2, 3]], 1),
    ([[72, 98], [62, 27], [32, 7], [71, 4], [25, 19], [91, 30], [52, 73], [10, 9], [99, 71], [47, 22], [19, 30],
      [80, 63], [18, 15], [48, 17], [77, 16], [46, 27], [66, 87], [55, 84], [65, 38], [30, 9], [50, 42], [100, 60],
      [75, 73], [98, 53], [22, 80], [41, 61], [37, 47], [95, 8], [51, 81], [78, 79], [57, 95]], 29),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minimumLines, cases)

if __name__ == '__main__':
    pass
