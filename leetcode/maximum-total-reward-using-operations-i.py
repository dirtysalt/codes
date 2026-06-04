#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        from sortedcontainers import SortedSet
        sl = SortedSet([0])
        rewardValues.sort()

        for x in rewardValues:
            tmp = []
            for y in sl:
                if y >= x: break
                tmp.append(x + y)
            sl.update(tmp)

        return sl[-1]


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 1, 3, 3], 4)
]

aatest_helper.run_test_cases(Solution().maxTotalReward, cases)

if __name__ == '__main__':
    pass
