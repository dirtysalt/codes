#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        graph = [set() for _ in range(n)]

        indices = {}
        for idx, w in enumerate(words):
            indices[w] = idx

        for idx, w in enumerate(words):
            for p in range(len(w)):
                t = w[:p] + w[p + 1:]
                idx2 = indices.get(t)
                if idx2 is not None:
                    graph[idx].add(idx2)

        cache = [0] * n

        def f(v):
            if cache[v] != 0:
                return cache[v]

            res = 0
            for v2 in graph[v]:
                res = max(res, f(v2))

            res += 1
            cache[v] = res
            return res

        ans = 0
        for i in range(n):
            ans = max(ans, f(i))
        return ans


cases = [
    (["a", "b", "ba", "bca", "bda", "bdca"], 4)
]
import aatest_helper

aatest_helper.run_test_cases(Solution().longestStrChain, cases)
