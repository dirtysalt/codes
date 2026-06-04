#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        from collections import defaultdict
        taken = defaultdict(int)
        for r, c in reservedSeats:
            r, c = r - 1, c - 1
            taken[r] = taken[r] | (1 << c)

        ans = n * 2
        for r, st in taken.items():
            a, b, c = (st >> 1) & 0xf, (st >> 3) & 0xf, (st >> 5) & 0xf
            if a == 0 and c == 0:
                pass
            elif a == 0 or b == 0 or c == 0:
                ans -= 1
            else:
                ans -= 2
            # print('{} {:b}, {}'.format(r, st, ans))
        return ans


cases = [
    (3, [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]], 4),
    (4, [[4, 3], [1, 4], [4, 6], [1, 7]], 4),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxNumberOfFamilies, cases)
