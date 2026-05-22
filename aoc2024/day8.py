#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import string


def solve(grid):
    n, m = len(grid), len(grid[0])
    from collections import defaultdict
    pos = defaultdict(list)
    for i in range(n):
        for j in range(m):
            c = grid[i][j]
            if c in string.digits or c in string.ascii_letters:
                pos[c].append((i, j))

    # print(pos)
    pts = []

    def ok(i, j):
        for c in pos:
            ps = pos[c]
            for x0, y0 in ps:
                for x1, y1 in ps:
                    if (x0, y0) == (x1, y1): continue
                    if (i - x0) * 2 == (i - x1) and (j - y0) * 2 == (j - y1):
                        # print(i, j, x0, y0, x1, y1, c)
                        return True
        return False

    for i in range(n):
        for j in range(m):
            if ok(i, j):
                pts.append((i, j))
    # print(pts)
    return len(pts)


def main():
    input = 'tmp.in'
    ans = 0
    grid = []
    with open(input) as fh:
        for s in fh:
            s = s.strip()
            if not s: continue
            grid.append(s)
    print(solve(grid))


if __name__ == '__main__':
    main()
