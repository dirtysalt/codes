#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        s, e = (1 << 63) - 1, 0
        for x, y, l in squares:
            s = min(y, s)
            e = max(y + l, e)

        def test(yline):
            upper, lower = 0, 0
            for x, y, l in squares:
                if y >= yline:
                    upper += l * l
                elif (y + l) <= yline:
                    lower += l * l
                else:
                    lower += (yline - y) * l
                    upper += (y + l - yline) * l
            return upper, lower

        for _ in range(50):
            m = (s + e) * 0.5
            upper, lower = test(m)
            if upper > lower:
                s = m
            else:
                e = m
        return m


true, false, null = True, False, None
import aatest_helper

cases = [
    ([[0, 0, 1], [2, 2, 1]], 1.00),
    ([[0, 0, 2], [1, 1, 1]], 1.16667)
]

aatest_helper.run_test_cases(Solution().separateSquares, cases)

if __name__ == '__main__':
    pass
