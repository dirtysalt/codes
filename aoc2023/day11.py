#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(grid):
    grid2 = []
    for i in range(len(grid)):
        grid2.append(grid[i])
        if all((x == '.' for x in grid[i])):
            grid2.append(grid[i])

    def transpose(x):
        n, m = len(x), len(x[0])
        res = [[' '] * n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                res[j][i] = x[i][j]
        return res

    grid = transpose(grid2)
    grid2 = []
    for i in range(len(grid)):
        grid2.append(grid[i])
        if all((x == '.' for x in grid[i])):
            grid2.append(grid[i])

    grid = transpose(grid2)
    n, m = len(grid), len(grid[0])
    pts = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#':
                pts.append((i, j))

    ans = 0
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            x0, y0 = pts[i]
            x1, y1 = pts[j]
            ans += abs(x1 - x0) + abs(y1 - y0)
    return ans


def main():
    # test = True
    test = False
    input_file = 'tmp.in' if test else 'input.txt'

    ans = 0
    grid = []
    with open(input_file) as fh:
        for s in fh:
            s = s.strip()
            grid.append(list(s))
    ans = solve(grid)
    print(ans)
    return ans


if __name__ == '__main__':
    main()
