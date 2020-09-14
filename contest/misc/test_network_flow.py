#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from graph_util import Graph, parse_graph_in_text


def find_augmenting_path(G: Graph, s, t):
    n = len(G)
    inf = 1 << 30

    flow = [0] * n
    flow[s] = inf
    visit = [0] * n
    parent = [-1] * n  # 如果选取这个节点的话，那么从哪个点流向这个点

    mat = G.mat
    # 类似Dijkstra算法，不过选择最大的一个flow做扩展
    while True:
        max_flow = 0
        max_node = None
        for x in range(n):
            # 选择一个点做扩展
            if flow[x] > max_flow and not visit[x]:
                max_flow = flow[x]
                max_node = x

        if max_node is None:
            break

        x = max_node
        visit[x] = 1
        for y, edge_value in enumerate(mat[x]):
            if not visit[y]:
                # 更新到达这个点的最大流
                value = min(max_flow, edge_value)
                if value > flow[y]:
                    flow[y] = value
                    parent[y] = x

    # 回溯求出增广通路
    edges = []
    if flow[t] != 0:
        x = t
        while x != s:
            edges.append((parent[x], x, flow[x]))
            x = parent[x]
        edges = edges[::-1]

    # 返回所选择的边和这条边上的最大流
    return edges, flow[t]


def update_redisual_graph(G, edges):
    mat = G.mat

    # 更新正向边权重，并且增加一条反向边
    for (x, y, v) in edges:
        mat[x][y] -= v
        mat[y][x] += v

    return G


def test_find_aug_path():
    text = """
         s a 3 b 2
         a b 1 c 2 d 4
         b d 2
         c t 2
         d t 3
      """
    G = parse_graph_in_text(text)
    edges, flow = find_augmenting_path(G, G.find_node_by_name('s'), G.find_node_by_name('t'))
    print(G.readable_edges(edges), flow)


def find_network_flow(G, s, t):
    res = 0
    while True:
        edges, flow = find_augmenting_path(G, s, t)
        if flow == 0:
            break
        res += flow
        print(G.readable_edges(edges), flow)
        update_redisual_graph(G, edges)
    return res


def test_find_network_flow():
    text = """
       s a 3 b 2
       a b 1 c 2 d 4
       b d 2
       c t 2
       d t 3
    """

    text = """
    s a 1000000 b 1000000
    a b 1 t 1000000
    b t 1000000
    """

    G = parse_graph_in_text(text)
    res = find_network_flow(G, G.find_node_by_name('s'), G.find_node_by_name('t'))
    print(res)


print('test_find_aug_path')
test_find_aug_path()

print('test_find_network_flow')
test_find_network_flow()
