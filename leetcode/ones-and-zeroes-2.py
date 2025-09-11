#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        N = len(strs)
        cnt = [[0, 0] for _ in range(N)]
        for i, s in enumerate(strs):
            a, b = 0, 0
            for c in s:
                if c == '0':
                    a += 1
                else:
                    b += 1
            cnt[i][0] = a
            cnt[i][1] = b

            # print(cnt)

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        ans = 0
        for i in range(N):
            a, b = cnt[i]
            for x in reversed(range(m - a + 1)):
                for y in reversed(range(n - b + 1)):
                    res = dp[x + a][y + b] = max(dp[x + a][y + b], dp[x][y] + 1)
                    ans = max(res, ans)
        return ans
