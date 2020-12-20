#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        n = len(grid)
        if n == 0: return 0
        m = len(grid[0])
        if m == 0: return 0

        nm = n * m
        sizes = {}
        paths = [-1] * nm

        def dfs(r, c, parent):
            idx = r * m + c
            if paths[idx] != -1:
                return 0
            paths[idx] = parent
            res = 1
            for dr, dc in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                r2 = r + dr
                c2 = c + dc
                if 0 <= r2 < n and 0 <= c2 < m \
                        and grid[r2][c2] == 1 \
                        and paths[r2 * m + c2] == -1:
                    res += dfs(r2, c2, parent)
            return res

        for r in range(n):
            for c in range(m):
                idx = r * m + c
                if grid[r][c] == 1:
                    res = dfs(r, c, idx)
                    if res != 0:
                        sizes[idx] = res

        def fill(r, c):
            res = 1
            ps = []
            for dr, dc in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                r2 = r + dr
                c2 = c + dc
                if 0 <= r2 < n and 0 <= c2 < m and grid[r2][c2] == 1:
                    idx = r2 * m + c2
                    pidx = paths[idx]
                    if pidx not in ps:
                        ps.append(pidx)
                        res += sizes[pidx]
            return res

        res = 0
        if sizes:
            res = max(sizes.values())
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 0:
                    out = fill(r, c)
                    if out > res:
                        res = out
        return res


if __name__ == '__main__':
    sol = Solution()
    grid = [[1, 0], [0, 1]]
    print(sol.largestIsland(grid))
    grid = [[1, 1], [0, 1]]
    print(sol.largestIsland(grid))
