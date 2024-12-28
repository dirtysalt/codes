#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def solve(grid):
    n, m = len(grid), len(grid[0])
    x, y = 0, 0
    d = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '^':
                x, y = i, j
    dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visit = set()
    while 0 <= x < n and 0 <= y < m:
        visit.add((x, y))
        while True:
            dx, dy = dxy[d]
            x2, y2 = x + dx, y + dy
            if not (0 <= x2 < n and 0 <= y2 < m):
                break
            if not grid[x2][y2] == '#':
                break
            d = (d + 1) % 4
        x, y = x2, y2
    return len(visit)


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
