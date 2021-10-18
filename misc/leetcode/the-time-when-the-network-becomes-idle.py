#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        n = len(patience)
        adj = [[] for _ in range(n)]
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        inf = 1 << 30
        dist = [inf] * n

        hp = []
        import heapq
        hp.append((0, 0))
        dist[0] = 0

        while hp:
            (d, x) = heapq.heappop(hp)
            for y in adj[x]:
                if dist[y] == inf:
                    dist[y] = d + 1
                    heapq.heappush(hp, (d + 1, y))

        # print(dist)

        ans = 0
        for i in range(1, n):
            t = dist[i]
            p = patience[i]
            res = 2 * t
            if 2 * t > p:
                r = (2 * t) % p
                if r == 0:
                    r = p
                res += (2 * t) - r
            ans = max(ans, res)
        return ans + 1


true, false, null = True, False, None
cases = [
    ([[0, 1], [1, 2]], [0, 2, 1], 8),
    ([[0, 1], [0, 2], [1, 2]], [0, 10, 10], 3),
    ([[0, 1]], [0, 100000], 3),
    ([[3, 8], [4, 13], [0, 7], [0, 4], [1, 8], [14, 1], [7, 2], [13, 10], [9, 11], [12, 14], [0, 6], [2, 12], [11, 5],
      [6, 9], [10, 3]], [0, 3, 2, 1, 5, 1, 5, 5, 3, 1, 2, 2, 2, 2, 1], 20),
    ([[5, 7], [15, 18], [12, 6], [5, 1], [11, 17], [3, 9], [6, 11], [14, 7], [19, 13], [13, 3], [4, 12], [9, 15],
      [2, 10], [18, 4], [5, 14], [17, 5], [16, 2], [7, 1], [0, 16], [10, 19], [1, 8]],
     [0, 2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1], 67),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().networkBecomesIdle, cases)

if __name__ == '__main__':
    pass
