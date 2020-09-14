#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = {}

        def f(x):
            if x in dp:
                return dp[x]

            opts = []
            if x < n - 1:
                max_value = arr[x + 1]
                for j in range(x + 1, min(x + d + 1, n)):
                    max_value = max(max_value, arr[j])
                    if arr[x] > max_value:
                        opts.append(j)
                    else:
                        break

            if x > 0:
                max_value = arr[x - 1]
                for j in reversed(range(max(0, x - d), x)):
                    max_value = max(max_value, arr[j])
                    if arr[x] > max_value:
                        opts.append(j)
                    else:
                        break

            # print(x, opts)
            ans = 0
            for j in opts:
                ans = max(f(j), ans)
            ans += 1
            dp[x] = ans
            return ans

        ans = 0
        for x in range(n):
            ans = max(ans, f(x))
        return ans
