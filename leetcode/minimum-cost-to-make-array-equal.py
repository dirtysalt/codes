#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        n = len(nums)
        ps = list(zip(nums, cost))
        ps.sort()

        res = 0
        for i in range(n):
            res += (ps[i][0] - ps[0][0]) * ps[i][1]
        ans = res
        tc = sum(cost)
        c = 0
        for i in range(1, n):
            d = ps[i][0] - ps[i - 1][0]
            c += ps[i - 1][1]
            l = d * c
            r = d * (tc - c)
            res = res + l - r
            ans = min(ans, res)
        return ans


true, false, null = True, False, None
cases = [
    ([1, 3, 5, 2], [2, 3, 1, 14], 8),
    ([2, 2, 2, 2, 2], [4, 2, 8, 1, 3], 0),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minCost, cases)

if __name__ == '__main__':
    pass
