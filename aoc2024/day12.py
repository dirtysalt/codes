#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(grid):
    n, m = len(grid), len(grid[0])
    from collections import defaultdict
    regions = defaultdict(set)
    visit = set()

    def dfs(c, i, j, ps):
        if (i, j) in ps:
            return
        ps.add((i, j))
        for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            x, y = i + dx, j + dy
            if 0 <= x < n and 0 <= y < m and grid[x][y] == c:
                dfs(c, x, y, ps)

    def fence_len(ps):
        group = defaultdict(list)
        for x, y in ps:
            group[x].append(y)
        res = 0
        for x, ys in group.items():
            for y in ys:
                if x == 0 or grid[x - 1][y] != grid[x][y]:
                    res += 1
                if (x + 1) == n or grid[x + 1][y] != grid[x][y]:
                    res += 1
                if y == 0 or grid[x][y - 1] != grid[x][y]:
                    res += 1
                if (y + 1) == m or grid[x][y + 1] != grid[x][y]:
                    res += 1
        return res

    ans = 0
    for i in range(n):
        for j in range(m):
            c = grid[i][j]
            if (i, j) in visit: continue
            ps = set()
            dfs(c, i, j, ps)
            visit.update(ps)
            r = fence_len(ps)
            # print(c, len(ps), r)
            ans += r * len(ps)
    return ans


def main():
    input = 'tmp.in'
    grid = []
    with open(input) as fh:
        for s in fh:
            s = s.strip()
            grid.append(s)
    print(solve(grid))


if __name__ == '__main__':
    main()
