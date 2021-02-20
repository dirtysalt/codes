#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import random


# 1. 静态确定选择顺序，选择顺序上做改进
# 2. 动态选择顺序，如何动态调整？

# def Run1(n, edges):
#     hp = []
#     for i in range(n):
#         hp.append((len(edges[i]), i))
#     hp.sort()
#     exclude = set()
#     ans = [0] * n
#     k = 0
#     for i in range(n):
#         d, x = hp[i]
#         if x in exclude:
#             continue
#         exclude.add(x)
#         ans[x] = 1
#         k += 1
#         exclude.update(edges[x])
#     return k, ans

def Run1(n, edges):
    from collections import defaultdict
    dist = defaultdict(list)
    for i in range(n):
        x = len(edges[i])
        dist[x].append(i)
    keys = list(dist.keys())
    keys.sort()

    def make_order(seed):
        random.seed(seed)
        res = []
        for k in keys:
            xs = dist[k]
            random.shuffle(xs)
            res += xs
        return res

    def run(order):
        exclude = set()
        ans = [0] * n
        k = 0
        for x in order:
            if x in exclude:
                continue
            exclude.add(x)
            ans[x] = 1
            k += 1
            exclude.update(edges[x])
        return k, ans

    res = None
    max_k = 0
    for i in range(100):
        order = make_order(i)
        k, ans = run(order)
        if k > max_k:
            max_k = k
            # print('AAA', max_k)
            res = ans

    return max_k, res


def Run2(n, edges):
    deg = [0] * n
    hp = []
    for i in range(n):
        hp.append((len(edges[i]), i))
        deg[i] = len(edges[i])

    import heapq
    heapq.heapify(hp)

    exclude = set()
    ans = [0] * n
    k = 0
    while hp:
        (d, x) = heapq.heappop(hp)
        if x in exclude:
            continue
        exclude.add(x)
        ans[x] = 1
        k += 1
        new_ex = []
        for y in edges[x]:
            if y not in exclude:
                exclude.add(y)
                new_ex.append(y)
        for y in new_ex:
            for z in edges[y] - exclude:
                if ans[z] == 0:
                    deg[z] = min(deg[z] - 1, 30)
                    hp.append((deg[z], z))
    return k, ans


# this is codeforces main function


def main():
    from sys import stdin

    def read_int():
        return int(stdin.readline())

    def read_int_array(sep=None):
        return [int(x) for x in stdin.readline().split(sep)]

    def read_str_array(sep=None):
        return [x.strip() for x in stdin.readline().split(sep)]

    import os

    if os.path.exists('tmp.in'):
        stdin = open('tmp.in')

    n, m = read_int_array()
    edges = [set() for _ in range(n)]
    global E
    E = edges
    for i in range(m):
        a, b = read_int_array()
        edges[a - 1].add(b - 1)
        edges[b - 1].add(a - 1)
    k, ans = Run1(n, edges)
    assert k == sum(ans)
    print(k)
    print(' '.join(str(x) for x in ans))


if __name__ == '__main__':
    main()
