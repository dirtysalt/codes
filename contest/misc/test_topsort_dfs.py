#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from graph_util import Graph, parse_graph_in_text


def topsort_dfs(G: Graph):
    # 使用满足拓扑排序要求的顺序进行DFS，之后逆序输出
    # 这些节点就满足拓扑排序要求
    visited = set()
    orders = []
    n = len(G)

    def fn(v):
        visited.add(v)
        for x in range(n):
            if G.mat[v][x] != 0 and x not in visited:
                fn(x)
        orders.append(v)

    for v in range(n):
        if v in visited:
            continue
        fn(v)

    return orders[::-1]


def test_topsort_dfs():
    text = """
    MAC3311 MAD2104
    COP3210 MAD2104 COP3400 COP3337
    MAD2104 CAP3700 MAD3305 MAD3512 COP3530 CDA4101 CDA4400
    COP3400 CDA4101
    COP3337 COP3530 CDA4101 COP4555
    MAD3512 COP5621
    COP3530 COP4540 COP4610 CIS4610
    CDA4101 COP4610
    CIS4610 COP5621
    COP4610 COP4225
    """
    G = parse_graph_in_text(text, weighted=False)
    orders = topsort_dfs(G)
    for v in orders:
        print(G.get_node_name(v))


test_topsort_dfs()
