#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(grid):
    n, m = len(grid), len(grid[0])
    sz = [[-1] * m for _ in range(n)]
    from collections import deque
    q = deque()

    si, sj = 0, 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'S':
                si, sj = i, j
                break

    map = {
        'F': [(0, 1), (1, 0)],
        '7': [(0, -1), (1, 0)],
        'L': [(0, 1), (-1, 0)],
        'J': [(0, -1), (-1, 0)],
        '-': [(0, -1), (0, 1)],
        '|': [(1, 0), (-1, 0)]
    }

    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        i2, j2 = si + dx, sj + dy
        if not (0 <= i2 < n and 0 <= j2 < m):
            continue
        c = grid[i2][j2]
        if c not in map: continue
        ok = False
        for dx2, dy2 in map[c]:
            if i2 + dx2 == si and j2 + dy2 == sj:
                ok = True
                break
        if ok:
            q.append((i2, j2, 1))

    while q:
        (i, j, d) = q.popleft()
        if sz[i][j] != -1: continue
        sz[i][j] = d
        c = grid[i][j]
        if c not in map: continue
        for dx, dy in map[c]:
            i2, j2 = i + dx, j + dy
            if 0 <= i2 < n and 0 <= j2 < m and sz[i2][j2] == -1:
                q.append((i2, j2, d + 1))

    print(sz)
    ans = 0
    for i in range(n):
        for j in range(m):
            ans = max(ans, sz[i][j])
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
            grid.append(s)
    ans = solve(grid)
    print(ans)
    return ans


if __name__ == '__main__':
    main()
