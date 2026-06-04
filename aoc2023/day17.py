#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import heapq


def solve(grid):
    n, m = len(grid), len(grid[0])

    q = []
    q.append((0, 0, -1, 'r'))
    q.append((0, -1, 0, 'd'))

    direction = {
        'r': (0, 1),
        'l': (0, -1),
        'u': (-1, 0),
        'd': (1, 0),
    }
    visit = {}
    while q:
        c, x, y, d = heapq.heappop(q)
        key = (x, y, d)
        if key in visit: continue
        print(key, c)
        visit[key] = c
        dx, dy = direction[d]

        cost = c
        dirs = 'ud' if d in 'lr' else 'lr'
        for k in range(1, 3 + 1):
            x2, y2 = x + k * dx, y + k * dy
            if not (0 <= x2 < n and 0 <= y2 < m): break
            cost += grid[x2][y2]
            for d2 in dirs:
                key = (x2, y2, d2)
                if key in visit: continue
                heapq.heappush(q, (cost, x2, y2, d2))

    ans = 1 << 63
    for d in 'lrdu':
        key = (n - 1, m - 1, d)
        if key in visit:
            ans = min(ans, visit[key])
    return ans - grid[0][0]


def main():
    # test = True
    test = False
    input_file = 'tmp.in' if test else 'input.txt'
    grid = []
    with open(input_file) as fh:
        for s in fh:
            s = s.strip()
            grid.append([int(x) for x in s])
    ans = solve(grid)
    print(ans)


if __name__ == '__main__':
    main()
