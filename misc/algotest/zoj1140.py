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
        # path = []
        while ending != 0:
            p = parent[ending]
            matching[ending] = p
            matching[p] = ending
            ending = parent[p]
    return matching


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

    if os.path.exists('../local/tmp.in'):
        stdin = open('../local/tmp.in')

    cases = read_int()
    for _ in range(cases):
        P, N = read_int_array()
        adj = [[] for _ in range(P + N + 1)]
        for p in range(P):
            xs = read_int_array()[1:]
            for x in xs:
                adj[p + 1].append(P + x)
                adj[P + x].append(p + 1)
        matching = hungarian(adj)
        res = 0
        for x in matching:
            if matching[x] != 0:
                res += 1
        if res == 2 * P:
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()
