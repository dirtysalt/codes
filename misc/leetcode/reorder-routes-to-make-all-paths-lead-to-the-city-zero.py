#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        fwd = [[] for _ in range(n)]
        back = [[] for _ in range(n)]
        for a, b in connections:
            fwd[a].append(b)
            back[b].append(a)

        from collections import deque
        dq = deque()
        visit = [0] * n
        dq.append(0)
        ans = 0
        while dq:
            x = dq.popleft()
            visit[x] = 1
            for y in back[x]:
                if visit[y] == 0:
                    visit[y] = 1
                    dq.append(y)
            for y in fwd[x]:
                # change direction.
                if visit[y] == 0:
                    visit[y] = 1
                    dq.append(y)
                    ans += 1
        return ans
