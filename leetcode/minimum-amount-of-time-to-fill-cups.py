#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        ans = 0

        amount = amount.copy()
        amount.sort()
        idx = 0
        while True:
            if amount[-1] == 0:
                break
            while amount[idx] == 0:
                idx += 1
            if idx == 2:
                ans += amount[-1]
                break

            ans += 1
            amount[idx] -= 1
            amount[-1] -= 1
            amount.sort()
        return ans


true, false, null = True, False, None
cases = [
    ([1, 4, 2], 4),
    ([5, 4, 4], 7),
    ([5, 0, 0], 5),
    ([0, 2, 2], 2)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().fillCups, cases)

if __name__ == '__main__':
    pass
