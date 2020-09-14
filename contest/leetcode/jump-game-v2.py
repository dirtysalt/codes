#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        A = list(range(n))
        A.sort(key=lambda x: arr[x])
        dp = [0] * n

        for i in A:
            # to left
            res = 0
            for j in reversed(range(max(i - d, 0), i)):
                if arr[i] > arr[j]:
                    res = max(res, dp[j])
                else:
                    break

            # to right
            for j in range(i + 1, min(i + d + 1, n)):
                if arr[i] > arr[j]:
                    res = max(res, dp[j])
                else:
                    break

            # print(i)
            dp[i] = res + 1

        # print(dp)
        ans = max(dp)
        return ans
