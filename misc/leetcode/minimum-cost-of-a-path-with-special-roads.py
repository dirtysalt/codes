#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import heapq
from typing import List


class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        if start == target: return 0
        pos = {}
        back = []

        def addPos(xy):
            (x, y) = xy
            if (x, y) in pos: return
            idx = len(pos)
            pos[(x, y)] = idx
            back.append((x, y))

        addPos(start)
        addPos(target)
        for (a, b, c, d, e) in specialRoads:
            addPos((a, b))
            addPos((c, d))

        n = len(pos)
        INF = 1 << 30
        adj = [[INF] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                x, y = back[i]
                u, v = back[j]
                c = abs(x - u) + abs(y - v)
                adj[i][j] = adj[j][i] = c

        for (a, b, c, d, e) in specialRoads:
            i = pos[(a, b)]
            j = pos[(c, d)]
            if adj[i][j] > e:
                adj[i][j] = e

        print(n)
        dp = [INF] * n
        hp = []
        hp.append((0, 0))
        while hp:
            (d, x) = heapq.heappop(hp)
            if dp[x] != INF: continue
            dp[x] = d
            for y in range(n):
                if dp[y] == INF:
                    heapq.heappush(hp, (d + adj[x][y], y))
        return dp[1]


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 1], [4, 5], [[1, 2, 3, 3, 2], [3, 4, 4, 5, 1]], 5),
    ([3, 2], [5, 7], [[3, 2, 3, 4, 4], [3, 3, 5, 5, 5], [3, 4, 5, 6, 6]], 7),
    ([1, 1], [10, 4], [[4, 2, 1, 1, 3], [1, 2, 7, 4, 4], [10, 3, 6, 1, 2], [6, 1, 1, 2, 3]], 8),
    ([1, 1], [1, 1], [[1, 1, 1, 1, 1], [1, 1, 1, 1, 5], [1, 1, 1, 1, 1]], 0),
]

# cases += aatest_helper.read_cases_from_file('tmp.in', 4)

aatest_helper.run_test_cases(Solution().minimumCost, cases)

if __name__ == '__main__':
    pass
