#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def test(t, c):
            for r in ranks:
                x = int((t / r) ** 0.5)
                if (x + 1) ** 2 * r <= t:
                    x += 1
                c -= x
                if c <= 0:
                    return True
            return False

        s, e = 1, max(ranks) * (cars ** 2)
        while s <= e:
            m = (s + e) // 2
            if test(m, cars):
                e = m - 1
            else:
                s = m + 1
        ans = s
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([4, 2, 3, 1], 10, 16),
    ([5, 1, 8], 6, 16),
    ([3], 52, 8112),
]

aatest_helper.run_test_cases(Solution().repairCars, cases)

if __name__ == '__main__':
    pass
