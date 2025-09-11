#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from collections import deque


class Solution:
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """

        n = len(quiet)
        adj = [[] for _ in range(n)]
        ins = [0] * n
        ans = [-1] * n

        for (x, y) in richer:
            adj[x].append(y)
            ins[y] += 1

        queue = deque()
        for i in range(n):
            ans[i] = i
            if ins[i] == 0:
                queue.append(i)

        while queue:
            x = queue.popleft()
            for y in adj[x]:
                if quiet[ans[y]] > quiet[ans[x]]:
                    ans[y] = ans[x]
                ins[y] -= 1
                if ins[y] == 0:
                    queue.append(y)

        return ans
