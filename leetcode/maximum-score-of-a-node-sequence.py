#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        n = len(scores)
        adj = [[] for _ in range(n)]
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        for i in range(n):
            adj[i].sort(key=lambda x: scores[x], reverse=True)

        ans = -1
        for x, y in edges:
            for z0 in adj[x][:3]:
                if z0 == y: continue
                for z1 in adj[y][:3]:
                    if z1 == x or z1 == z0: continue
                    res = scores[x] + scores[y] + scores[z0] + scores[z1]
                    ans = max(ans, res)
        return ans


if __name__ == '__main__':
    pass
