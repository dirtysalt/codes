#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        index = {}
        for i, w in enumerate(words):
            index[w] = i

        n = len(words)
        adj = [[] for _ in range(n)]

        for i, w in enumerate(words):
            for j in range(len(w) + 1):
                for x in range(26):
                    w2 = w[:j] + chr(x + ord('a')) + w[j:]
                    if w2 in index:
                        k = index[w2]
                        adj[i].append(k)

        depth = [0] * n

        def dfs(u):
            if depth[u] != 0:
                return depth[u]

            d = 0
            for v in adj[u]:
                d = max(d, dfs(v))
            depth[u] = d + 1
            return d + 1

        ans = 0
        for i in range(n):
            d = dfs(i)
            ans = max(ans, d)
        return ans


cases = [
    (["a", "b", "ba", "bca", "bda", "bdca"], 4)
]
import aatest_helper

aatest_helper.run_test_cases(Solution().longestStrChain, cases)
