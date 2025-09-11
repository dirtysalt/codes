#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        adj = [[] for _ in range(n)]
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        def dfs(x, parent, target):
            s = nums[x]

            for y in adj[x]:
                if y == parent: continue
                res = dfs(y, x, target)
                if res < 0:
                    return -1
                s += res

            if s > target:
                return -1
            if s == target:
                return 0
            return s

        M = max(nums)
        total = sum(nums)
        part = total // M
        for p in reversed(range(1, part + 1)):
            if total % p == 0:
                target = total // p
                assert target >= M
                if dfs(0, -1, target) == 0:
                    return p - 1


true, false, null = True, False, None
cases = [
    ([6, 2, 2, 2, 6], [[0, 1], [1, 2], [1, 3], [3, 4]], 2),
    ([2], [], 0),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().componentValue, cases)

if __name__ == '__main__':
    pass
