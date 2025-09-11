#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        n = len(nums)
        adj = [[] for _ in range(n)]
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        primes = [[] for _ in range(51)]
        for x in range(1, 51):
            for y in range(x, 51):
                g = gcd(x, y)
                if g == 1:
                    primes[x].append(y)
                    primes[y].append(x)

        last = [-1] * 51
        timestamp = [0] * n
        ans = [-1] * n

        def dfs(x, ts):
            v = nums[x]
            res = None
            for p in primes[v]:
                if last[p] == -1: continue
                if res is None or timestamp[last[p]] > timestamp[res]:
                    res = last[p]
            ans[x] = -1 if res is None else res

            old = last[v]
            last[v] = x
            timestamp[x] = ts
            ts += 1
            for y in adj[x]:
                if timestamp[y]: continue
                dfs(y, ts)
                ts += 1
            last[v] = old

        dfs(0, 1)
        return ans


cases = [
    ([2, 3, 3, 2], [[0, 1], [1, 2], [1, 3]], [-1, 0, 0, 1]),
    ([5, 6, 10, 2, 3, 6, 15], [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]], [-1, 0, -1, 0, 0, 0, -1]),
    (
        [9, 16, 30, 23, 33, 35, 9, 47, 39, 46, 16, 38, 5, 49, 21, 44, 17, 1, 6, 37, 49, 15, 23, 46, 38, 9, 27, 3, 24, 1,
         14,
         17, 12, 23, 43, 38, 12, 4, 8, 17, 11, 18, 26, 22, 49, 14, 9],
        [[17, 0], [30, 17], [41, 30], [10, 30], [13, 10], [7, 13], [6, 7], [45, 10], [2, 10], [14, 2], [40, 14],
         [28, 40],
         [29, 40], [8, 29], [15, 29], [26, 15], [23, 40], [19, 23], [34, 19], [18, 23], [42, 18], [5, 42], [32, 5],
         [16, 32], [35, 14], [25, 35], [43, 25], [3, 43], [36, 25], [38, 36], [27, 38], [24, 36], [31, 24], [11, 31],
         [39, 24], [12, 39], [20, 12], [22, 12], [21, 39], [1, 21], [33, 1], [37, 1], [44, 37], [9, 44], [46, 2],
         [4, 46]],
        [-1, 21, 17, 43, 10, 42, 7, 13, 29, 44, 17, 31, 39, 10, 10, 29, 32, 0, 40, 23, 12, 39, 12, 40, 25, 35, 15, 38,
         40,
         40, 17, 24, 5, 1, 19, 14, 17, 21, 25, 24, 14, 17, 40, 25, 37, 17, 10]),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().getCoprimes, cases)
