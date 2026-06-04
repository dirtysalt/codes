#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        import heapq
        pq = []
        pq.append((0, 0, 0))
        ans = {}
        inf = (1 << 63) - 1
        while pq:
            t, x, y = heapq.heappop(pq)
            if (x, y) in ans: continue
            ans[(x, y)] = t
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x2, y2 = x + dx, y + dy
                if 0 <= x2 < n and 0 <= y2 < m and (x2, y2) not in ans:
                    cost = max(t, moveTime[x2][y2]) + 1
                    if cost < ans.get((x2, y2), inf):
                        heapq.heappush(pq, (cost, x2, y2))
        return ans[(n - 1, m - 1)]


true, false, null = True, False, None
import aatest_helper

cases = [
    ([[0, 4], [4, 4]], 6),
    ([[0, 0, 0], [0, 0, 0]], 3),
    ([[0, 1], [1, 2]], 3),
]

aatest_helper.run_test_cases(Solution().minTimeToReach, cases)

if __name__ == '__main__':
    pass
