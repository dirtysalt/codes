#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        dist = {}

        from collections import deque
        def prepare():
            q = deque()
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == 1:
                        dist[(i, j)] = 0
                        q.append((i, j, 0))

            while q:
                (i, j, d) = q.popleft()
                for dx, dy in ((-1, 0), (0, 1), (0, -1), (1, 0)):
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < m and (x, y) not in dist:
                        dist[(x, y)] = (d + 1)
                        q.append((x, y, d + 1))

        prepare()

        def run():
            visited = set()
            import heapq
            ans = 10000
            hp = [(-dist[(0, 0)], 0, 0)]
            visited.add((0, 0))

            while hp:
                d, i, j = heapq.heappop(hp)
                ans = min(ans, -d)

                if (i, j) == (n - 1, m - 1):
                    break

                for dx, dy in ((-1, 0), (0, 1), (0, -1), (1, 0)):
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < m and (x, y) not in visited:
                        visited.add((x, y))
                        heapq.heappush(hp, (-dist[(x, y)], x, y))
            return ans

        return run()


true, false, null = True, False, None
import aatest_helper

cases = [
    ([[1, 0, 0], [0, 0, 0], [0, 0, 1]], 0),
    ([[0, 0, 1], [0, 0, 0], [0, 0, 0]], 2),
    ([[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]], 2),
    ([[0, 1, 1], [0, 1, 1], [1, 1, 1]], 0),
]
cases += aatest_helper.read_cases_from_file('tmp.in', 2)
aatest_helper.run_test_cases(Solution().maximumSafenessFactor, cases)

if __name__ == '__main__':
    pass
