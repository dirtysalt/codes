#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        X = max(nums)
        if X == 0:
            return 0
        n = len(nums)
        dp = [[0] * (X + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = 1

        for idx, (l, r, val) in enumerate(queries):
            for i in range(l, r + 1):
                for x in reversed(range(X + 1)):
                    if dp[i][x] == 1 and (val + x) <= X:
                        dp[i][val + x] = 1

            if all(dp[i][nums[i]] for i in range(n)):
                return idx + 1
        return -1


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(nums=[2, 0, 2], queries=[[0, 2, 1], [0, 2, 1], [1, 1, 3]], res=2),
    aatest_helper.OrderedDict(nums=[4, 3, 2, 1], queries=[[1, 3, 2], [0, 2, 1]], res=-1),
    aatest_helper.OrderedDict(nums=[1, 2, 3, 2, 1], queries=[[0, 1, 1], [1, 2, 1], [2, 3, 2], [3, 4, 1], [4, 4, 1]],
                              res=4),
    aatest_helper.OrderedDict(nums=[1, 2, 3, 2, 6],
                              queries=[[0, 1, 1], [0, 2, 1], [1, 4, 2], [4, 4, 4], [3, 4, 1], [4, 4, 5]], res=4),
]

aatest_helper.run_test_cases(Solution().minZeroArray, cases)

if __name__ == '__main__':
    pass
