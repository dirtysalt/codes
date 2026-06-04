#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:

        def bfs(max_weight):
            adj = [set() for _ in range(n)]
            fwd = [set() for _ in range(n)]
            for x, y, w in edges:
                if w > max_weight: continue
                if x in adj[y]:  continue
                adj[y].add(x)

            from collections import deque
            q = deque()
            visited = set()
            q.append(0)
            while q:
                x = q.popleft()
                visited.add(x)
                for y in adj[x]:
                    if y in visited: continue
                    visited.add(y)
                    fwd[y].add(x)
                    q.append(y)

            if len(visited) != n:
                return False

            for x in range(n):
                if len(fwd[x]) > threshold:
                    return False

            return True

        max_weight = max([x[2] for x in edges])
        s, e = 0, max_weight
        while s <= e:
            m = (s + e) // 2
            if bfs(m):
                e = m - 1
            else:
                s = m + 1
        if s > max_weight: return -1
        return s


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(n=5, edges=[[1, 0, 1], [2, 0, 2], [3, 0, 1], [4, 3, 1], [2, 1, 1]], threshold=2, res=1),
    aatest_helper.OrderedDict(n=5, edges=[[0, 1, 1], [0, 2, 2], [0, 3, 1], [0, 4, 1], [1, 2, 1], [1, 4, 1]],
                              threshold=1, res=-1),
    aatest_helper.OrderedDict(n=5, edges=[[1, 2, 1], [1, 3, 3], [1, 4, 5], [2, 3, 2], [3, 4, 2], [4, 0, 1]],
                              threshold=1, res=2),
    aatest_helper.OrderedDict(n=5, edges=[[1, 2, 1], [1, 3, 3], [1, 4, 5], [2, 3, 2], [4, 0, 1]], threshold=1, res=-1),
    (4, [[2, 0, 39], [2, 1, 72], [2, 3, 67], [1, 2, 78], [3, 0, 10], [0, 2, 81]], 2, 78),
]

aatest_helper.run_test_cases(Solution().minMaxWeight, cases)

if __name__ == '__main__':
    pass
