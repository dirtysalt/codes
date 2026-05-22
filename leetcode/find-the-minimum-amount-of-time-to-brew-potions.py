#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n, m = len(skill), len(mana)
        times = [0] * (n + 1)
        for i in range(n):
            times[i + 1] = times[i] + mana[0] * skill[i]
        # print(times)

        for j in range(1, m):
            X = times[1]
            for i in range(1, n):
                X += skill[i - 1] * mana[j]
                X = max(X, times[i + 1])
            X += mana[j] * skill[-1]

            times[-1] = X
            for i in reversed(range(n)):
                times[i] = times[i + 1] - mana[j] * skill[i]

        return times[-1]


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(skill=[1, 5, 2, 4], mana=[5, 1, 4, 2], res=110),
    aatest_helper.OrderedDict(skill=[1, 1, 1], mana=[1, 1, 1], res=5),
    aatest_helper.OrderedDict(skill=[1, 2, 3, 4], mana=[1, 2], res=21),
]

aatest_helper.run_test_cases(Solution().minTime, cases)

if __name__ == '__main__':
    pass
