#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        ans = []
        used = [0] * n

        def dfs(sz, path):
            if sz == n:
                ans.append(path.copy())
                return

            from collections import defaultdict
            opts = defaultdict(list)
            for i in range(n):
                if used[i] or (path and path[-1] == nums[i]):
                    continue
                x = nums[i]
                opts[x].append(i)

            for x, idxs in opts.items():
                sz2 = sz
                for idx in idxs:
                    used[idx] = 1
                    path.append(x)
                    sz2 += 1
                    dfs(sz2, path)

                for idx in idxs:
                    sz2 -= 1
                    used[idx] = 0
                    path.pop()

        dfs(0, [])
        ans.sort()
        return ans
