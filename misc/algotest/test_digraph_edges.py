#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# 计算各种边的类型，对于无向图有树边(tree edge)和反向边(backward edge).
# 有向图还包括正向边(forward edge)和交叉变(cross edge).
# 各种边的类型都可以通过扩展DFS算法来计算

from graph_util import Graph, parse_graph_in_text


class State:
    def __init__(self, n):
        self.ts = 0
        self.in_ts = [-1] * n
        self.out_ts = [-1] * n
        self.ps_ts = [-1] * n
        self.parents = [-1] * n

    def enter(self, v):
        self.in_ts[v] = self.ts
        self.ts += 1

    def exit(self, v):
        self.out_ts[v] = self.ts
        self.ts += 1

    def process(self, v):
        self.ps_ts[v] = self.ts
        self.ts += 1

    def set_parent(self, v, p):
        self.parents[v] = p

    def get_parent(self, v):
        return self.parents[v]


def di_dfs(G: Graph, ss):
    n = len(G)
    tree_edges = []
    back_edges = []
    fwd_edges = []
    cross_edges = []

    state = State(n)

    def fn(v):
        state.enter(v)
        state.process(v)
        mat = G.mat
        for v2 in range(n):
            if mat[v][v2] != 0:
                # 如果没有访问的话，那么记录下parent关系，这个在判断是否为回边的时候需要去除
                if state.in_ts[v2] == -1:
                    state.set_parent(v2, v)
                    tree_edges.append((v, v2))
                    fn(v2)


                # 如果 v->v2, 但是v2访问的时间更早并且不是父子关系的话，那么认为是回边
                # 并且要求这个时候v2还没有访问完成
                elif state.get_parent(v) != v2 and \
                        state.in_ts[v] > state.in_ts[v2] and \
                        state.out_ts[v2] == -1:
                    back_edges.append((v, v2))

                else:
                    assert (state.out_ts[v2] != -1)
                    # 如果v2访问完成时间是大于v访问初始时间，那么就是正向边
                    if state.out_ts[v2] > state.in_ts[v]:
                        fwd_edges.append((v, v2))
                    else:
                        cross_edges.append((v, v2))

        state.exit(v)

    for s in ss:
        fn(s)
    return state, tree_edges, back_edges, fwd_edges, cross_edges


def test_di_dfs():
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
    ss = [G.find_node_by_name(x) for x in ('b', 'h', 'g')]
    state, tree_edges, back_edges, fwd_edges, cross_edges = di_dfs(G, ss)

    print('===== tree edges =====')
    res = G.readable_edges(tree_edges)
    for x in res:
        print(x)
    print('===== back edges =====')
    res = G.readable_edges(back_edges)
    for x in res:
        print(x)
    print('===== fwd edges =====')
    res = G.readable_edges(fwd_edges)
    for x in res:
        print(x)
    print('===== cross edges =====')
    res = G.readable_edges(cross_edges)
    for x in res:
        print(x)
    print('==== state =====')
    n = len(G)
    for v in range(n):
        print('node {}: in_ts = {}, out_ts = {}'.format(
            G.get_node_name(v),
            state.in_ts[v], state.out_ts[v]))


test_di_dfs()
