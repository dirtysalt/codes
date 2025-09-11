#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans = 0
        now = capacity

        for i in range(len(plants)):
            p = plants[i]
            if p <= now:
                now -= p
                ans += 1
            else:
                dist = (p + capacity - 1) // capacity
                now = dist * capacity - p
                step = 2 * dist * (i + 1) - 1
                ans += step
        return ans


true, false, null = True, False, None
cases = [
    ([2, 2, 3, 3], 5, 14),
    ([1, 1, 1, 4, 2, 3], 4, 30),
    ([7, 7, 7, 7, 7, 7, 7], 8, 49),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().wateringPlants, cases)

if __name__ == '__main__':
    pass
