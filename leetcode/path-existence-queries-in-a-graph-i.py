#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        # find upper
        upper = [0] * n
        j = 0
        for i in range(n):
            while j < n and nums[j] - nums[i] <= maxDiff:
                j += 1
            upper[i] = (j - 1)

        # compress upper
        for i in reversed(range(n)):
            upper[i] = upper[upper[i]]

        ans = []
        for u, v in queries:
            if u > v:
                u, v = v, u
            ans.append(upper[u] >= v)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(n=2, nums=[1, 3], maxDiff=1, queries=[[0, 0], [0, 1]], res=[true, false]),
    aatest_helper.OrderedDict(n=4, nums=[2, 5, 6, 8], maxDiff=2, queries=[[0, 1], [0, 2], [1, 3], [2, 3]],
                              res=[false, false, true, true]),
]

aatest_helper.run_test_cases(Solution().pathExistenceQueries, cases)

if __name__ == '__main__':
    pass
