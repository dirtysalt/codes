#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import random


class Graph:
    def __init__(self, mat, names):
        self.mat = mat
        # 节点名称
        self.names = names
        self.name_to_idx = {k: v for v, k in enumerate(names)}

    def find_node_by_name(self, name):
        return self.name_to_idx[name]

    def get_node_name(self, x):
        return self.names[x]

    def __len__(self):
        return len(self.mat)

    def readable_edges(self, edges):
        res = []
        for edge in edges:
            e = list(edge)
            e[0] = self.get_node_name(e[0])
            e[1] = self.get_node_name(e[1])
            res.append(e)
        return res


def parse_graph_in_text(text, directional=True, weighted=True):
    """将text解析为图数据，这样创建节点比较容易"""
    edges = []
    nodes = {}
    for s in text.split('\n'):
        s = s.strip()
        if not s:
            continue

        # 强制节点顺序
        if s.startswith('#'):
            if s.startswith('#V:'):
                s = s[len('#V:'):]
                ss = s.split()
                for x in ss:
                    x = x.strip()
                    if x not in nodes:
                        nodes[x] = len(nodes)
            continue

        ss = s.split()
        src = ss[0]
        if src not in nodes:
            nodes[src] = len(nodes)

        dsts = []
        if weighted:
            for i in range(1, len(ss), 2):
                t, v = ss[i], int(ss[i + 1])
                dsts.append((t, v))
        else:
            dsts.extend((t, 1) for t in ss[1:])

        for t, v in dsts:
            if t not in nodes:
                nodes[t] = len(nodes)
            edges.append((nodes[src], nodes[t], v))
            if not directional:
                edges.append((nodes[t], nodes[src], v))

    n = len(nodes)
    mat = []
    for i in range(n):
        mat.append([0] * n)
    for (x, y, v) in edges:
        mat[x][y] = v

    names = [''] * n
    for name, idx in nodes.items():
        names[idx] = name

    G = Graph(mat, names)
    return G


def generate_maze(n, m):
    # 起始点始终是0,0
    my, mx = n, m
    maze = [[0 for x in range(mx)] for y in range(my)]
    dx = [0, 1, 0, -1];
    dy = [-1, 0, 1, 0]  # 4 directions to move in the maze
    color = [(0, 0, 0), (255, 255, 255)]  # RGB colors of the maze
    # start the maze from a random cell
    # stack = [(random.randint(0, mx - 1), random.randint(0, my - 1))]
    stack = [(0, 0)]
    while len(stack) > 0:
        (cx, cy) = stack[-1]
        maze[cy][cx] = 1

        # find a new cell to add
        nlst = []  # list of available neighbors
        for i in range(4):
            nx = cx + dx[i];
            ny = cy + dy[i]
            if nx >= 0 and nx < mx and ny >= 0 and ny < my:
                if maze[ny][nx] == 0:
                    # of occupied neighbors must be 1
                    ctr = 0
                    for j in range(4):
                        ex = nx + dx[j];
                        ey = ny + dy[j]
                        if ex >= 0 and ex < mx and ey >= 0 and ey < my:
                            if maze[ey][ex] == 1: ctr += 1
                    if ctr == 1: nlst.append(i)
        # if 1 or more neighbors available then randomly select one and move
        if len(nlst) > 0:
            ir = nlst[random.randint(0, len(nlst) - 1)]
            cx += dx[ir];
            cy += dy[ir]
            stack.append((cx, cy))
        else:
            stack.pop()
    return maze


def patch_1s(maze, ratio=0.25):
    n, m = len(maze), len(maze[0])
    ps = []
    for x in range(n):
        for y in range(m):
            if maze[x][y] == 0:
                ps.append((x, y))
    visited = set()

    for i in range(int(n * m * ratio)):
        idx = random.randint(0, len(ps) - 1)
        if idx in visited:
            continue
        visited.add(idx)
        x, y = ps[idx]
        maze[x][y] = 1
