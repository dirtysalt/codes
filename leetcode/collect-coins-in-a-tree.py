#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        ind = [0] * n
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
            ind[x] += 1
            ind[y] += 1

        # remove leaf node coin = 0
        from collections import deque
        q = deque()
        for i in range(n):
            if ind[i] == 1 and coins[i] == 0:
                q.append(i)
        while q:
            x = q.popleft()
            for y in adj[x]:
                ind[y] -= 1
                if ind[y] == 1 and coins[y] == 0:
                    q.append(y)

        # walk from leaf node to mark depth.
        q = deque()
        depth = [0] * n
        for i in range(n):
            if ind[i] == 1 and coins[i]:
                q.append(i)
                depth[i] = 0

        while q:
            x = q.popleft()
            for y in adj[x]:
                ind[y] -= 1
                # won't lead to coins = 0 leaf.
                if ind[y] == 1:
                    depth[y] = depth[x] + 1
                    q.append(y)

        edge = len([x for x in range(n) if depth[x] >= 2]) - 1
        if edge < 0: return 0
        ans = 2 * edge
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 0, 0, 0, 0, 1], [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]], 2),
    ([0, 0, 0, 1, 1, 0, 0, 1], [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [5, 6], [5, 7]], 2),
    ([0, 0], [[0, 1]], 0),
    ([1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0],
     [[0, 1], [1, 2], [1, 3], [2, 4], [4, 5], [5, 6], [5, 7], [4, 8], [7, 9], [7, 10], [10, 11]], 4),
    ([1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0],
     [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5], [4, 6], [2, 7], [7, 8], [3, 9], [8, 10], [8, 11], [6, 12], [7, 13],
      [11, 14], [10, 15]], 4),
]

# cases += aatest_helper.read_cases_from_file('tmp.in', 3)

aatest_helper.run_test_cases(Solution().collectTheCoins, cases)

if __name__ == '__main__':
    pass
