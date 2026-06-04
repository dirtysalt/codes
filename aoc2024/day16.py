#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(grid):
    n, m = len(grid), len(grid[0])
    fx, fy = 0, 0
    import heapq
    from collections import defaultdict
    q = []
    cost = defaultdict(lambda: (1 << 30))
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'S':
                q.append((0, i, j, 0))
            elif grid[i][j] == 'E':
                fx, fy = i, j

    dxy = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    while q:
        d, i, j, k = heapq.heappop(q)
        if d >= cost[(i, j, k)]: continue
        cost[(i, j, k)] = d

        # keep moving
        dx, dy = dxy[k]
        x, y = i + dx, j + dy
        if 0 <= x < n and 0 <= y < m and grid[x][y] != '#':
            if (d + 1) < cost[(x, y, k)]:
                heapq.heappush(q, (d + 1, x, y, k))

        # turn
        if (d + 1000) < cost[(i, j, (k + 1) % 4)]:
            heapq.heappush(q, (d + 1000, i, j, (k + 1) % 4))
        if (d + 1000) < cost[(i, j, (k + 3) % 4)]:
            heapq.heappush(q, (d + 1000, i, j, (k + 3) % 4))

    ans = 1 << 30
    for k in range(4):
        if (fx, fy, k) in cost:
            ans = min(ans, cost[(fx, fy, k)])
    return ans


def main():
    input = 'tmp.in'
    grid = []
    with open(input) as fh:
        for s in fh:
            s = s.strip()
            if not s: break
            grid.append(list(s))
    print(solve(grid))


if __name__ == '__main__':
    main()
