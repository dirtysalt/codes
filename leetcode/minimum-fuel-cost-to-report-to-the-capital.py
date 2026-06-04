#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads) + 1
        adj = [[] for _ in range(n)]
        for x, y in roads:
            adj[x].append(y)
            adj[y].append(x)

        def dfs(x, px):
            # return [people, cost]
            # people: how many people in this city
            # cost: how much oil be used so far.
            P, C = 1, 0
            for y in adj[x]:
                if y != px:
                    p, c = dfs(y, x)
                    P, C = P + p, C + c
                    C += (p + seats - 1) // seats
            return P, C

        _, ans = dfs(0, -1)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([[0, 1], [0, 2], [0, 3]], 5, 3),
    ([[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]], 2, 7),
    ([], 1, 0),
]

aatest_helper.run_test_cases(Solution().minimumFuelCost, cases)

if __name__ == '__main__':
    pass
