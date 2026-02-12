#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        n = len(values)
        adj = [[] for _ in range(n)]

        for x, y, t in edges:
            adj[x].append((y, t))
            adj[y].append((x, t))

        visited = [0] * n
        ans = [0]
        path = []

        def dfs(x, t, res):
            if x == 0:
                # print(x, t, res, path)
                ans[0] = max(ans[0], res)

            for y, dt in adj[x]:
                if (t + dt) > maxTime: continue
                path.append(y)
                visited[y] += 1
                res2 = res
                if visited[y] == 1:
                    res2 += values[y]
                dfs(y, t + dt, res2)
                visited[y] -= 1
                path.pop()

        visited[0] = 1
        dfs(0, 0, values[0])

        return ans[0]


true, false, null = True, False, None
cases = [
    ([0, 32, 10, 43], [[0, 1, 10], [1, 2, 15], [0, 3, 10]], 49, 75),
    ([5, 10, 15, 20], [[0, 1, 10], [1, 2, 10], [0, 3, 10]], 30, 25),
    ([1, 2, 3, 4], [[0, 1, 10], [1, 2, 11], [2, 3, 12], [1, 3, 13]], 50, 7),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maximalPathQuality, cases)

if __name__ == '__main__':
    pass
