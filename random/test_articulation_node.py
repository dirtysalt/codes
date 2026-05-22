#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from graph_util import Graph, parse_graph_in_text


class State:
    def __init__(self, n):
        self.num = [-1] * n
        self.parent = [-1] * n
        self.low = [-1] * n
        self.counter = 0

    def assign_number(self, v):
        self.low[v] = self.counter
        self.num[v] = self.counter
        self.counter += 1


def find_articulation_nodes(G: Graph):
    # low[v] = min(num[v], min(low[x] for x in children), min(num[x] for (v, x) in back_edges)
    # low的含义是这个节点向上回溯，能关联到序号最低的节点是什么
    # 如果某个节点v，它其中一个孩子x, low[x] <= num[v]的话，说明这个x没有办法
    # 连接到序号更低的节点，那么v节点就是一个割点
    n = len(G)
    res = set()
    state = State(n)

    def fn(v):
        state.assign_number(v)
        for t in range(n):
            if G.mat[v][t] != 0:

                # tree edges.
                if state.num[t] == -1:
                    state.parent[t] = v
                    fn(t)

                    if state.low[t] >= state.num[v]:
                        # v is articulation node.
                        res.add(v)
                    state.low[v] = min(state.low[v], state.low[t])

                # back edges.
                elif state.parent[v] != t and state.num[v] > state.num[t]:
                    state.low[v] = min(state.low[v], state.num[t])

    start = 0
    fn(start)
    count = 0
    for t in range(n):
        if G.mat[start][t] != 0:
            count += 1
            if count >= 2:
                res.add(start)
                break
    return list(res)


def test_find_articulation_nodes():
    text = """
    a b d
    b a c
    c b d g
    d a c e f
    e d f
    f d e
    """
    G = parse_graph_in_text(text, weighted=False, directional=False)
    art_nodes = find_articulation_nodes(G)
    print('===== art nodes =====')
    for x in art_nodes:
        print(G.get_node_name(x))


test_find_articulation_nodes()
