#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        csum = sum(colsum)
        if csum != (upper + lower):
            return []
        sz2 = len([x for x in colsum if x == 2])
        if sz2 > lower or sz2 > upper:
            # print('got')
            return []

        ans = []
        n = len(colsum)
        for i in range(n):
            if colsum[i] == 0:
                ans.append((0, 0))
            elif colsum[i] == 1:
                if upper > 0 and upper >= lower:
                    upper -= 1
                    ans.append((1, 0))
                else:
                    lower -= 1
                    ans.append((0, 1))
            else:
                ans.append((1, 1))
                upper -= 1
                lower -= 1

        # print(ans, [x[0] + x[1] for x in ans])
        a, b = [x[0] for x in ans], [x[1] for x in ans]
        return [a, b]


cases = [
    (5, 5, [2, 1, 2, 0, 1, 0, 1, 2, 0, 1], [[1, 1, 1, 0, 1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 0, 0, 1, 1, 0, 1]]),
    (9, 2, [0, 1, 2, 0, 0, 0, 0, 0, 2, 1, 2, 1, 2], []),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().reconstructMatrix, cases)
