#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        from collections import deque
        visited = set()
        n, m = len(maze), len(maze[0])
        x, y = entrance

        dq = deque()
        dq.append((x, y, 0))
        visited.add((x, y))
        ans = -1
        while dq:
            x, y, d = dq.popleft()
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x2, y2 = x + dx, y + dy
                if 0 <= x2 < n and 0 <= y2 < m and (x2, y2) not in visited and maze[x2][y2] == '.':
                    if (x2 in (0, n - 1) or y2 in (0, m - 1)):
                        ans = d + 1
                        break
                    visited.add((x2, y2))
                    dq.append((x2, y2, d + 1))

            if ans != -1: break
        return ans


if __name__ == '__main__':
    pass
