#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        n = len(brackets)
        import copy
        bs = copy.deepcopy(brackets)
        for i in range(1, n):
            bs[i][0] -= brackets[i - 1][0]

        ans = 0
        for i in range(n):
            x = min(income, bs[i][0])
            p = bs[i][1]
            ans += x * p * 0.01
            income -= x
            if income <= 0: break

        return ans


true, false, null = True, False, None
cases = [
    ([[2, 7], [3, 17], [4, 37], [7, 6], [9, 83], [16, 67], [19, 29]], 18, 7.79),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().calculateTax, cases)

if __name__ == '__main__':
    pass
