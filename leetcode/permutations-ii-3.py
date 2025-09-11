#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        used = [0] * n
        ans = []

        def dfs(path):
            if len(path) == n:
                ans.append(path.copy())
                return

            for i in range(n):
                if used[i]:
                    continue
                if i > 0 and nums[i - 1] == nums[i] and not used[i - 1]:
                    continue

                used[i] = 1
                path.append(nums[i])
                dfs(path)
                path.pop()
                used[i] = 0

        dfs([])
        return ans
