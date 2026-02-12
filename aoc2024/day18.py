#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(n, m, corrupt, step):
    block = set(corrupt[:step])
    from collections import deque, defaultdict
    q = deque()
    cost = defaultdict(lambda: 1 << 30)
    q.append((0, 0, 0))
    while q:
        (d, x, y) = q.popleft()
        if d >= cost[(x, y)]: continue
        cost[x, y] = d
        if (x, y) == (n - 1, m - 1): break
        for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            x2, y2 = x + dx, y + dy
            if 0 <= x2 < n and 0 <= y2 < m and (x2, y2) not in block and (d + 1) < cost[(x2, y2)]:
                # print(x2, y2, d + 1)
                q.append((d + 1, x2, y2))
    return cost[(n - 1, m - 1)]


def main():
    input = 'tmp.in'
    corrupt = []
    with open(input) as fh:
        for s in fh:
            s = s.strip()
            if not s: continue
            corrupt.append(tuple([int(x) for x in s.split(',')]))
    n = m = 71
    step = 1024
    print(solve(n, m, corrupt, step))


if __name__ == '__main__':
    main()
