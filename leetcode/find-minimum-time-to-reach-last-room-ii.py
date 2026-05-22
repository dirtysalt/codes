#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        import heapq
        pq = []
        pq.append((0, 0, 0, 0))
        inf = (1 << 63) - 1
        ans = {}
        while pq:
            t, x, y, f = heapq.heappop(pq)
            if (x, y, f) in ans: continue
            ans[(x, y, f)] = t
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x2, y2 = x + dx, y + dy
                if 0 <= x2 < n and 0 <= y2 < m and (x2, y2) not in ans:
                    cost = max(t, moveTime[x2][y2]) + (1 if f == 0 else 2)
                    if cost < ans.get((x2, y2, 1 - f), inf):
                        # ans[(x2, y2, 1 - f)] = cost
                        heapq.heappush(pq, (cost, x2, y2, 1 - f))
        return min(ans.get((n - 1, m - 1, 0), inf), ans.get((n - 1, m - 1, 1), inf))


true, false, null = True, False, None
import aatest_helper

cases = [
    ([[0, 4], [4, 4]], 7),
    ([[0, 0, 0, 0], [0, 0, 0, 0]], 6),
    ([[0, 1], [1, 2]], 4),
]

aatest_helper.run_test_cases(Solution().minTimeToReach, cases)

if __name__ == '__main__':
    pass
