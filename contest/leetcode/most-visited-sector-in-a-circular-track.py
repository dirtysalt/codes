#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        vis = [0] * n
        for i in range(1, len(rounds)):
            a, b = rounds[i - 1], rounds[i]
            if i != 1:
                a += 1
            if b < a: b += n
            for j in range(a, b + 1):
                vis[(j - 1) % n] += 1

        val = max(vis)
        ans = []
        for i in range(n):
            if vis[i] == val:
                ans.append(i + 1)
        ans.sort()
        return ans
