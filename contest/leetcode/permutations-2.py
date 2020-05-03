#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)
        used = [False] * n

        def dfs(path):
            if len(path) == n:
                ans.append(path.copy())
                return

            for j in range(n):
                if not used[j]:
                    used[j] = True
                    path.append(nums[j])
                    dfs(path)
                    path.pop()
                    used[j] = False

        dfs([])
        return ans


cases = [
    ([1, 2, 3], [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1]
    ])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().permute, cases)
