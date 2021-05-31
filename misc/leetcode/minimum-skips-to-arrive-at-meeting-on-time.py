#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        n = len(dist)

        inf = 1 << 30
        dp = [[0] * (n + 1) for _ in range(2)]
        now = 0
        import math

        for i in range(n):
            for j in range(n + 1):
                if j > (i + 1): break

                # dp[i][j] 跑到i 这个位置已经休息了j次
                # dp[i][j] = dp[i-1][j] ,  dp[i-1][j-1]

                a = inf
                if j <= i:
                    a = dp[now][j] + dist[i]
                b = inf
                if j > 0:
                    b = (dp[now][j - 1] + dist[i] + speed - 1) // speed * speed

                dp[1 - now][j] = min(a, b)

            now = 1 - now
            # print(dp[now])

        maxrest = -1
        for j in range(n + 1):
            if dp[now][j] <= hoursBefore * speed:
                maxrest = j
        if maxrest == -1: return -1
        return n - maxrest


if __name__ == '__main__':
    pass
