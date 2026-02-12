#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        adj = [[] for _ in range(n)]
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        import functools
        @functools.cache
        def dfs(i, odd, p):
            value = nums[i]
            if odd:
                value = value ^ k

            opts = []
            for j in adj[i]:
                if j == p: continue
                r0 = dfs(j, 0, i)
                r1 = dfs(j, 1, i)
                opts.append((r0, r1))
            opts.sort(key=lambda x: - (x[1] - x[0]))

            base = 0
            for r0, r1 in opts:
                base += max(r0, r1)

            end = 0
            flip = 0
            while end < len(opts):
                diff = opts[end][1] - opts[end][0]
                if diff < 0: break
                flip = 1 - flip
                end += 1

            res = base + ((value ^ k) if flip else value)
            if end < len(opts):
                diff = opts[end][1] - opts[end][0]
                r0 = base + diff + (value if flip else (value ^ k))
                res = max(res, r0)
            if (end - 1) >= 0:
                diff = opts[end - 1][1] - opts[end - 1][0]
                r1 = base - diff + (value if flip else (value ^ k))
                res = max(res, r1)
            return res

        ans = dfs(0, 0, -1)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(nums=[1, 2, 1], k=3, edges=[[0, 1], [0, 2]], res=6),
    aatest_helper.OrderedDict(nums=[2, 3], k=7, edges=[[0, 1]], res=9),
    aatest_helper.OrderedDict(nums=[7, 7, 7, 7, 7, 7], k=3, edges=[[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]], res=42),
    ([24, 78, 1, 97, 44], 6, [[0, 2], [1, 2], [4, 2], [3, 4]], 260),
]

aatest_helper.run_test_cases(Solution().maximumValueSum, cases)

if __name__ == '__main__':
    pass
