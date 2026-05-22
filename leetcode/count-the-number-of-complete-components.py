#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [set() for _ in range(n)]
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)

        C = [-1] * n

        def dfs(x, c, vs):
            C[x] = c
            vs.append(x)
            for y in adj[x]:
                if C[y] == -1:
                    dfs(y, c, xs)

        def check(xs):
            for x in xs:
                for y in xs:
                    if x == y: continue
                    if y not in adj[x]:
                        return False
            return True

        CT = 0
        ans = 0
        for x in range(n):
            if C[x] == -1:
                xs = []
                dfs(x, CT, xs)
                if check(xs):
                    ans += 1
                CT += 1
        return ans


if __name__ == '__main__':
    pass
