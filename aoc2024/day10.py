#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def solve(grid, x, y):
    n, m = len(grid), len(grid[0])
    from collections import Counter
    q = Counter()
    q[(x, y)] = 1
    for _ in range(9):
        q2 = Counter()
        for (x, y), c in q.items():
            for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                x2, y2 = x + dx, y + dy
                if 0 <= x2 < n and 0 <= y2 < m and grid[x2][y2] == (grid[x][y] + 1):
                    q2[(x2, y2)] += c
        q = q2
        # print(q)

    ans = len(q)
    return ans


def solve_grid(grid):
    n, m = len(grid), len(grid[0])
    ans = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                ans += solve(grid, i, j)
    return ans


def main():
    input = 'tmp.in'
    grid = []
    with open(input) as fh:
        for s in fh:
            s = s.strip()
            grid.append([-1 if x == '.' else int(x) for x in s])
    print(solve_grid(grid))


if __name__ == '__main__':
    main()
