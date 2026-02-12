#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(grid):
    n, m = len(grid), len(grid[0])
    print(n, m)

    def bfs(i, j):
        if grid[i][j] not in 'SE.': return

        # right wall.
        ok = False
        if (j + 2) < m and grid[i][j + 1] == '#' and grid[i][j + 2] in 'SE.':
            ok = True

        # down wall
        if (i + 2) < n and grid[i + 1][j] == '#' and grid[i + 2][j] in 'SE.':
            ok = True

        if not ok: return
        from collections import deque, defaultdict
        q = deque()
        cost = defaultdict(lambda: 1 << 30)
        q.append((0, i, j))
        while q:
            d, x, y = q.popleft()
            if d >= cost[x, y]: continue
            cost[x, y] = d
            for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                x2, y2 = x + dx, y + dy
                if 0 <= x2 < n and 0 <= y2 < m and grid[x2][y2] != '#' and (d + 1) < cost[x2, y2]:
                    q.append((d + 1, x2, y2))

        save = []

        # right wall.
        if (j + 2) < m and grid[i][j + 1] == '#' and grid[i][j + 2] in 'SE.':
            save.append(cost[i, j + 2] - 2)

        # down wall
        if (i + 2) < n and grid[i + 1][j] == '#' and grid[i + 2][j] in 'SE.':
            save.append(cost[i + 2, j] - 2)

        # print(save)
        return save

    res = []
    for i in range(n):
        # kinda slow
        print(i)
        for j in range(m):
            # print(i, j)
            save = bfs(i, j)
            if not save: continue
            res.extend(save)

    return res


def main():
    input = 'tmp.in'
    grid = []
    with open(input) as fh:
        for s in fh:
            s = s.strip()
            if not s: continue
            grid.append(s)

    res = solve(grid)
    print(len([x for x in res if x >= 100]))


if __name__ == '__main__':
    main()
