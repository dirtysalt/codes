#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort()
        n = len(clips)

        adj = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if clips[j][0] <= clips[i][1]:
                    adj[i].append(j)

        from collections import deque
        dq = deque()
        depth = [0] * n
        for i in range(n):
            if clips[i][0] == 0:
                dq.append(i)
                depth[i] = 1

        ans = (n + 1)
        while dq:
            x = dq.popleft()
            if clips[x][1] >= T:
                ans = min(ans, depth[x])
                continue

            for y in adj[x]:
                if depth[y] != 0:
                    continue
                depth[y] = depth[x] + 1
                dq.append(y)
        if ans == (n + 1):
            ans = -1
        return ans
