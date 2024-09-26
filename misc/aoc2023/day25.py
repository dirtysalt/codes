#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import random
import sys

new_recursion_limit = 20000  # 设置为你想要的新深度
sys.setrecursionlimit(new_recursion_limit)


class UnionFind:
    def __init__(self, values):
        # r, c, = {}, {}
        n = len(values)
        r, c = [0] * n, [0] * n
        for v in values:
            r[v], c[v] = v, 1
        self.r, self.c = r, c

    def size(self, a):
        ra = self.find(a)
        return self.c[ra]

    def find(self, a):
        # find root.
        x = a
        while True:
            ra = self.r[x]
            if ra == x:
                break
            x = ra

        # compress path.
        x = a
        while x != ra:
            rx = self.r[x]
            self.r[x] = ra
            x = rx
        return ra

    def merge(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return rb
        ca, cb = self.c[ra], self.c[rb]
        if ca > cb:
            ca, cb, ra, rb = cb, ca, rb, ra
        self.r[ra] = rb
        self.c[rb] += ca
        return rb


# https://en.wikipedia.org/wiki/Karger%27s_algorithm
def karger(n, seed, edges):
    fu = UnionFind(list(range(n)))
    rnd = random.Random(seed)

    from collections import deque
    edges = edges.copy()
    rnd.shuffle(edges)
    Q = deque()
    for e in edges:
        Q.append(e)

    while n != 2:
        a, b = Q.popleft()
        a, b = fu.find(a), fu.find(b)
        if a == b: continue
        fu.merge(a, b)
        n -= 1

    left = 0
    root = set()
    while Q:
        a, b = Q.popleft()
        a, b = fu.find(a), fu.find(b)
        if a != b:
            left += 1
            root.add(a)
            root.add(b)

    if left == 3:
        assert len(root) == 2
        a, b = root
        a = fu.size(a)
        b = fu.size(b)
        return a * b
    return 0


def solve(graph):
    n = len(graph)
    edges = []
    for i in range(n):
        for j in graph[i]:
            if i < j:
                edges.append((i, j))
    print(n, len(edges))

    for seed in range(100000):
        print(f'running {seed}')
        ans = karger(n, seed, edges)
        if ans != 0:
            print(ans, seed)
            return ans


def main():
    # test = True
    test = False
    input_file = 'tmp.in' if test else 'input.txt'

    from collections import defaultdict
    adj = defaultdict(list)
    numbers = {}
    with open(input_file) as fh:
        for s in fh:
            s = s.strip()
            nodes = s.split()
            a = nodes[0][:-1]
            adj[a] = nodes[1:]

            # number it.
            if a not in numbers:
                numbers[a] = len(numbers)
            for b in adj[a]:
                if b not in numbers:
                    numbers[b] = len(numbers)

    graph = [set() for _ in range(len(numbers))]
    for f, xs in adj.items():
        fi = numbers[f]
        for x in xs:
            ti = numbers[x]
            graph[fi].add(ti)
            graph[ti].add(fi)

    ans = solve(graph)
    print(ans)


if __name__ == '__main__':
    main()
