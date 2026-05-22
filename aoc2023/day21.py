#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(grid, rep):
    n, m = len(grid), len(grid[0])
    visit = set()
    from collections import deque
    Q = deque()
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'S':
                Q.append((i, j, 0))

    while Q:
        x, y, d = Q.popleft()
        key = (x, y, d)
        if key in visit: continue
        visit.add(key)
        if (d + 1) > rep: continue
        for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            x2, y2 = x + dx, y + dy
            if 0 <= x2 < n and 0 <= y2 < m and grid[x2][y2] in 'S.':
                key = (x2, y2, d + 1)
                if key not in visit:
                    Q.append(key)

    res = {(x, y) for (x, y, d) in visit if d == rep}
    return len(res)


def main():
    # test = True
    test = False
    input_file = 'tmp.in' if test else 'input.txt'
    rep = 6 if test else 64
    grid = []
    with open(input_file) as fh:
        for s in fh:
            s = s.strip()
            grid.append(s)
    ans = solve(grid, rep)
    print(ans)


if __name__ == '__main__':
    main()
