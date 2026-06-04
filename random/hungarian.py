#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# https://www.renfei.org/blog/bipartite-matching.html

def hungarian(adj):
    n = len(adj)
    matching = [0] * n
    check = [0] * n
    parent = [0] * n
    from collections import deque
    dq = deque()

    for t in range(1, n):
        if matching[t] != 0: continue

        dq.clear()
        dq.append(t)
        check[t] = t
        parent[t] = 0
        ending = 0
        while dq and ending == 0:
            u = dq.popleft()
            for v in adj[u]:
                if check[v] == t: continue
                check[v] = t
                parent[v] = u
                if matching[v] == 0:
                    ending = v
                    break
                else:
                    parent[matching[v]] = v
                    dq.append(matching[v])

        # found a augmented path.
        # ending -> p[ending] -> .. x -> t -> 0
        path = []
        while ending != 0:
            p = parent[ending]
            path.append(ending)
            path.append(p)
            matching[ending] = p
            matching[p] = ending
            ending = parent[p]
        path = path[::-1]
        print('augpath', path)
    return matching


def build_adj(edges):
    n = 0
    n = max(n, max((x[0] for x in edges)))
    n = max(n, max((x[1] for x in edges)))
    adj = [[] for _ in range(n + 1)]
    for x, y in edges:
        adj[x].append(y)
        adj[y].append(x)
    return adj


def print_matching(matching):
    print(matching)
    n = len(matching)
    res = []
    for i in range(n):
        if matching[i] != -1 and matching[i] > i:
            res.append((i, matching[i]))
    print(res)


def main():
    # edges = [[1, 5], [1, 7], [2, 5], [3, 5], [3, 6], [4, 7], [4, 8]]
    edges = [[1, 6], [1, 8], [2, 6], [3, 6], [3, 7], [4, 8], [4, 9]]
    adj = build_adj(edges)
    print(adj)
    matching = hungarian(adj)
    print_matching(matching)


if __name__ == '__main__':
    main()
