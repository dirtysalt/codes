#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from graph_util import Graph, parse_graph_in_text


def find_scc(G: Graph):
    # 首先DFS对G里面每个节点进行拓扑排序
    # 然后按照拓扑顺序，对G'(G的反向图)做DFS.
    # 每次得到的一个component就是strongly connected component.

    n = len(G)

    # 先求解拓扑序
    visited = set()
    orders = []

    def dfs_fwd(v):
        visited.add(v)
        for x in range(n):
            if G.mat[v][x] != 0 and x not in visited:
                dfs_fwd(x)
        orders.append(v)

    for v in range(n):
        if v not in visited:
            dfs_fwd(v)

    orders = orders[::-1]

    # 基于拓扑序在反向图遍历
    res = []
    scc = set()
    visited = set()

    def dfs_back(v):
        scc.add(v)
        for x in range(n):
            if G.mat[x][v] != 0 and x not in visited:
                visited.add(x)
                dfs_back(x)

    for v in orders:
        if v not in visited:
            scc = set()
            dfs_back(v)
            res.append(scc)

    return res


def test_find_scc():
    text = """
    #V: a b c d e f g h i j
    a b d    
    b c f 
    c a d e
    d e
    f c
    g f h
    h f j
    i h
    j i
    """
    G = parse_graph_in_text(text, weighted=False)
    res = find_scc(G)
    for idx, scc in enumerate(res):
        print('SCC#{}: {}'.format(idx, [G.get_node_name(x) for x in scc]))


test_find_scc()
