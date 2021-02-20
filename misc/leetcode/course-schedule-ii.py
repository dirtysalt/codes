#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses

        adj = [[] for _ in range(n)]
        ind = [0] * n
        for (x, y) in prerequisites:
            adj[y].append(x)
            ind[x] += 1

        from collections import deque
        dq = deque()
        for x in range(n):
            if ind[x] == 0:
                dq.append(x)

        ans = []
        while dq:
            x = dq.popleft()
            ans.append(x)
            for y in adj[x]:
                ind[y] -= 1
                if ind[y] == 0:
                    dq.append(y)
        if len(ans) != n:
            ans = []
        return ans
