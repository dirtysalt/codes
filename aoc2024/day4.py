#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def flat(grid):
    n, m = len(grid), len(grid[0])
    for i in range(n):
        for j in range(m - 3):
            yield grid[i][j:j + 4]

    for j in range(m):
        for i in range(n - 3):
            buf = []
            for k in range(4):
                buf.append(grid[i + k][j])
            yield ''.join(buf)

    for x, y in [(0, j) for j in range(m)] + [(i, 0) for i in range(1, n)]:
        while x < n and y < m:
            buf = []
            for k in range(4):
                if (x + k) < n and (y + k) < m:
                    buf.append(grid[x + k][y + k])
            yield ''.join(buf)
            x += 1
            y += 1

    for x, y in [(0, j) for j in range(m)] + [(i, m - 1) for i in range(1, n)]:
        while x < n and y >= 0:
            buf = []
            for k in range(4):
                if (x + k) < n and (y - k) >= 0:
                    buf.append(grid[x + k][y - k])
            yield ''.join(buf)
            x += 1
            y -= 1


def solve(grid):
    ans = 0
    for t in flat(grid):
        if t == 'XMAS' or t == 'SAMX':
            ans += 1
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
