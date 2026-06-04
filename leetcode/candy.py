#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 0:
            return 0
        adj = [[] for _ in range(n)]
        ind = [0] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                adj[i - 1].append(i)
                ind[i] += 1
            elif ratings[i] < ratings[i - 1]:
                adj[i].append(i - 1)
                ind[i - 1] += 1

        # print(adj, ind)
        depth = [0] * n
        from collections import deque
        dq = deque()
        for i in range(n):
            if ind[i] == 0:
                dq.append(i)
                depth[i] = 1

        while dq:
            x = dq.popleft()
            d = depth[x]
            for y in adj[x]:
                ind[y] -= 1
                if ind[y] == 0:
                    depth[y] = d + 1
                    dq.append(y)

        ans = sum(depth)
        return ans
