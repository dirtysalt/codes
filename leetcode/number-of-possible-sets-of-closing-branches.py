#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        def find_state(st):
            sz = 0
            newx = [-1] * n
            for i in range(n):
                if st & (1 << i):
                    newx[i] = sz
                    sz += 1

            INF = 1 << 30
            adj = [[INF] * sz for _ in range(sz)]
            for i in range(sz):
                adj[i][i] = 0
            for i, j, w in roads:
                x, y = newx[i], newx[j]
                if x != -1 and y != -1:
                    adj[x][y] = min(adj[x][y], w)
                    adj[y][x] = min(adj[y][x], w)

            for k in range(sz):
                for i in range(sz):
                    for j in range(sz):
                        adj[i][j] = min(adj[i][k] + adj[k][j], adj[i][j])

            for i in range(sz):
                for j in range(sz):
                    if adj[i][j] > maxDistance:
                        return False
            return True

        ans = 0
        for st in range(1 << n):
            ok = find_state(st)
            if ok:
                ans += 1
        return ans


if __name__ == '__main__':
    pass
