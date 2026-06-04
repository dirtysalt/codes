#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


def get_primes(N):
    ps = []
    mask = [0] * (N + 1)
    for i in range(2, N + 1):
        if mask[i] == 1: continue
        for j in range(2, N + 1):
            if i * j > N: break
            mask[i * j] = 1
    for i in range(2, N + 1):
        if mask[i] == 0:
            ps.append(i)
    return ps


class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        primes = set(get_primes(n))
        adj = [[] for _ in range(n + 1)]
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        ans = 0

        def dfs(x, p):
            nonlocal ans
            isPrime = x in primes

            c0, c1 = 0, 0
            for y in adj[x]:
                if y == p: continue
                a, b = dfs(y, x)
                if isPrime:
                    ans += c0 * a
                else:
                    ans += c0 * b + c1 * a
                c0 += a
                c1 += b

            if isPrime:
                ans += c0
                res = (0, c0 + 1)
            else:
                ans += c1
                res = (c0 + 1, c1)

            # print(x, ans)
            return res

        dfs(1, -1)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    (5, [[1, 2], [1, 3], [2, 4], [2, 5]], 4),
    (6, [[1, 2], [1, 3], [2, 4], [3, 5], [3, 6]], 6),
]

aatest_helper.run_test_cases(Solution().countPaths, cases)

if __name__ == '__main__':
    pass
