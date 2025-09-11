#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        max_score = 0
        max_st = 0
        for st in range(1 << 12):
            t = 0
            score = 0
            for i in range(12):
                if st & (1 << i):
                    t += aliceArrows[i] + 1
                    score += i
            if t <= numArrows:
                if score > max_score:
                    max_score = score
                    max_st = st

        ans = [0] * 12
        for i in range(12):
            if max_st & (1 << i):
                ans[i] = aliceArrows[i] + 1
        rest = numArrows - sum(ans)
        ans[0] += rest
        return ans


true, false, null = True, False, None
cases = [
    (9, [1, 1, 0, 1, 0, 0, 2, 1, 0, 1, 2, 0], [0, 0, 0, 0, 1, 1, 0, 0, 1, 2, 3, 1],),
    (3, [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2], [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0]),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maximumBobPoints, cases)

if __name__ == '__main__':
    pass
