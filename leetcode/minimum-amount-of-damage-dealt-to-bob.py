#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        n = len(damage)
        idx = list(range(n))

        def f(x):
            r = (health[x] + power - 1) // power
            return r / damage[x]

        idx.sort(key=f)
        total = sum(damage)

        ans = 0
        for i in idx:
            r = (health[i] + power - 1) // power
            ans += r * total
            total -= damage[i]
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    (4, [1, 2, 3, 4], [4, 5, 6, 8], 39),
    (1, [1, 1, 1, 1], [1, 2, 3, 4], 20),
    (8, [40], [59], 320),
]

aatest_helper.run_test_cases(Solution().minDamage, cases)

if __name__ == '__main__':
    pass
