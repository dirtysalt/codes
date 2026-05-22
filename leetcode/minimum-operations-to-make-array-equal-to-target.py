#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        delta = [x - y for x, y in zip(nums, target)]
        n = len(delta)

        def sgn(d):
            if d == 0: return 0
            if d > 0: return 1
            return -1

        def handle(s, e):
            res, last = 0, 0
            for x in delta[s:e + 1]:
                x = abs(x)
                if x > last: res += x - last
                last = x
            return res

        ans, j = 0, 0
        for i in range(n):
            if i == n - 1 or sgn(delta[i + 1]) != sgn(delta[j]):
                ans += handle(j, i)
                j = i + 1
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([3, 5, 1, 2], [4, 6, 2, 4], 2),
    ([1, 3, 2], [2, 1, 4], 5),
    ([9, 2, 6, 10, 4, 8, 3, 4, 2, 3], [9, 5, 5, 1, 7, 9, 8, 7, 6, 5], 20)
]

aatest_helper.run_test_cases(Solution().minimumOperations, cases)

if __name__ == '__main__':
    pass
