#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        n = len(grid)
        inf = 1<<30
        minh = [[inf] * n for _ in range(n)]

        from collections import deque
        dq = deque()
        dq.append((0, 0))
        minh[0][0] = grid[0][0]
        S = set()
        S.add((0, 0))

        while dq:
            x, y = dq.popleft()
            S.remove((x, y))
            h = minh[x][y]

            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x2, y2 = x + dx, y + dy
                if not (0 <= x2 < n and 0 <= y2 <n):
                    continue
                old = minh[x2][y2]
                new = max(grid[x2][y2], min(h, old))
                minh[x2][y2] = new
                if new != old and (x2, y2) not in S:
                    dq.append((x2, y2))
                    S.add((x2, y2))

        return minh[n-1][n-1]

cases = [
    ([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]], 16),
    ([[0,2],[1,3]], 3),
]

import aatest_helper
aatest_helper.run_test_cases(Solution().swimInWater, cases)


if __name__ == '__main__':
    pass
