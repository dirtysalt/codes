#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(insts):
    x, y = 0, 0
    map = {
        'R': (0, 1),
        'L': (0, -1),
        'U': (-1, 0),
        'D': (1, 0),
    }
    trace = [(x, y)]
    first = True
    for d, k, _ in insts:
        dx, dy = map[d]
        k = int(k)
        if first:
            k -= 1
            first = False
        for _ in range(k):
            x, y = x + dx, y + dy
            trace.append((x, y))
    # print(trace)

    xs = [x[0] for x in trace]
    ys = [x[1] for x in trace]
    minx, maxx, miny, maxy = min(xs), max(xs), min(ys), max(ys)
    n, m = maxx - minx + 1, maxy - miny + 1

    grid = [['.'] * m for _ in range(n)]
    for x, y in trace:
        grid[x - minx][y - miny] = '#'

    for g in grid: print(g)

    from collections import deque
    q = deque()

    def dfs(x, y):
        q.append((x, y))

    for i in range(n):
        if grid[i][0] == '.':
            dfs(i, 0)
        if grid[i][-1] == '.':
            dfs(i, m - 1)
    for j in range(m):
        if grid[0][j] == '.':
            dfs(0, j)
        if grid[n - 1][j] == '.':
            dfs(n - 1, j)

    visit = set()
    while q:
        x, y = q.popleft()
        if (x, y) in visit: continue
        visit.add((x, y))
        for dx, dy in map.values():
            x2, y2 = x + dx, y + dy
            if 0 <= x2 < n and 0 <= y2 < m and grid[x2][y2] == '.' and (x2, y2) not in visit:
                q.append((x2, y2))

    return n * m - len(visit)


def main():
    # test = True
    test = False
    input_file = 'tmp.in' if test else 'input.txt'
    insts = []
    with open(input_file) as fh:
        for s in fh:
            s = s.strip()
            insts.append(s.split())

    ans = solve(insts)
    print(ans)


if __name__ == '__main__':
    main()
