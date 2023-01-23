#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(grid, n, m):
    visited = []
    for _ in range(n):
        visited.append([0] * m)

    def bfs(i, j):
        queue = list()
        queue.append((i, j))
        while queue:
            (i, j) = queue[0]
            queue.pop(0)
            for (dx, dy) in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                x = i + dx
                y = j + dy
                if 0 <= x < n and 0 <= y < m and not visited[x][y] and grid[x][y] == 'X':
                    visited[x][y] = 1
                    queue.append((x, y))

    # for i in range(n):
    #     print(grid[i])

    component = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] or grid[i][j] != 'X':
                continue
            # print('start with {}'.format((i, j)))
            component += 1
            visited[i][j] = 1
            bfs(i, j)
    return component


t = int(input())
for _ in range(t):
    n, m = input().rstrip().split()
    n, m = int(n), int(m)
    grid = input().rstrip().split()
    print(solve(grid, n, m))
