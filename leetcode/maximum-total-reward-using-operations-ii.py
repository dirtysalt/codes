#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        f = 1

        for v in sorted(set(rewardValues)):
            f |= (f & ((1 << v) - 1)) << v

        return f.bit_length() - 1


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 1, 3, 3], 4),
    ([1, 6, 4, 3, 2], 11),
    ([2, 15, 13, 3], 28)
]
# cases += [(list(range(50000)), 2)]

# cases += aatest_helper.read_cases_from_file('tmp.in',2)

aatest_helper.run_test_cases(Solution().maxTotalReward, cases)

if __name__ == '__main__':
    pass
