#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        def next_time(t):
            r = t // change
            if r % 2 == 0:
                return t + time
            return (r + 1) * change + time

        adj = [[] for _ in range(n)]
        for x, y in edges:
            x, y = x - 1, y - 1
            adj[x].append(y)
            adj[y].append(x)

        from collections import deque
        inf = 1 << 30
        dist = [(inf, inf) for _ in range(n)]
        Q = deque()
        Q.append((0, (0, inf)))

        while Q:
            x, up = Q.popleft()
            old = dist[x]

            # no need to update.
            if up[0] >= old[1]:
                continue

            if up[1] <= old[0]:
                new = up
            elif up[0] == old[0]:
                new = (up[0], min(old[1], up[1]))
            else:
                new = (min(up[0], old[0]), max(up[0], old[0]))

            if old == new:
                continue

            dist[x] = new
            a = min(next_time(new[0]), inf)
            b = min(next_time(new[1]), inf)
            up = (a, b)

            for y in adj[x]:
                # no need to update.
                if a >= dist[y][1]:
                    continue
                Q.append((y, up))

        if dist[-1][1] == inf:
            return next_time(next_time(dist[-1][0]))
        return dist[-1][1]


true, false, null = True, False, None
cases = [
    (5, [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]], 3, 5, 13,),
    (2, [[1, 2]], 3, 2, 11),
    (6, [[1, 2], [1, 3], [2, 4], [3, 5], [5, 4], [4, 6]], 3, 100, 12),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().secondMinimum, cases)

if __name__ == '__main__':
    pass
