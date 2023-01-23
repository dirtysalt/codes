#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from collections import deque

import heapq
import random

from graph_util import generate_maze, patch_1s

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def print_maze(maze):
    for x in maze:
        print(x)


def nns(maze, p):
    res = []
    x, y = p
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < len(maze) and ny >= 0 and ny < len(maze[0]):
            res.append((nx, ny))
    return res


def bfs(maze, src, dst):
    dq = deque()
    visited = set()
    dq.append((src, 0))
    visited.add(src)

    dist = -1
    while len(dq):
        p, d = dq.popleft()
        if p == dst:
            dist = d
            break

        for u in nns(maze, p):
            if maze[u[0]][u[1]] == 1 and u not in visited:
                visited.add(u)
                dq.append((u, d + 1))

    print('bfs: visited {} nodes, dist: {}'.format(len(visited), dist))
    return dist


def astar(maze, src, dst):
    def get_est_dist(p, to_src_dst):
        to_dst_dist = abs(p[0] - dst[0]) + abs(p[1] - dst[1])
        return to_dst_dist + to_src_dst

    nexts = []
    item = (get_est_dist(src, 0), src, 0)
    heapq.heappush(nexts, item)
    visited = set()
    visited.add(src)

    dist = -1

    while nexts:
        (est_dist, p, d) = heapq.heappop(nexts)
        if p == dst:
            dist = d
            break

        for u in nns(maze, p):
            if maze[u[0]][u[1]] == 1 and u not in visited:
                visited.add(u)
                item = (get_est_dist(u, d + 1), u, d + 1)
                heapq.heappush(nexts, item)

    print('astar: visited {} nodes, dist: {}'.format(len(visited), dist))
    return dist


def test_all():
    # random.seed(42)
    n, m = 200, 200
    maze = generate_maze(n, m)
    src = (0, 0)

    # 按照距离排序，然后选择中间某个点
    ps = []
    for x in range(n):
        for y in range(m):
            if maze[x][y] == 1:
                ps.append((x + y, x, y))
    ps.sort()
    # dst = ps[random.randint(len(ps) // 3, len(ps) * 2 // 3)][1:]
    dst = ps[-1][1:]

    patch_1s(maze)
    # print_maze(maze)
    print('find shortest path: {} -> {}'.format(src, dst))

    bfs(maze, src, dst)
    astar(maze, src, dst)


test_all()
