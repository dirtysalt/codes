#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        ans = []
        from collections import defaultdict

        def dfs(opts, path):
            # print(opts, path)
            if len(opts) == 0:
                ans.append(path.copy())
                return

            items = list(opts.items())
            for x, v in items:
                if path and path[-1] == x:
                    continue

                sz = len(path)
                for i in range(v):
                    opts[x] -= 1
                    if opts[x] == 0:
                        del opts[x]
                    path.extend([x] * (i + 1))
                    dfs(opts, path)
                    path = path[:sz]

                opts[x] = v

        opts = defaultdict(int)
        for x in nums:
            opts[x] += 1
        dfs(opts, [])
        ans.sort()
        return ans
