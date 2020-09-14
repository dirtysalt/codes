#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def integerBreak(self, n: int) -> int:

        import functools
        @functools.lru_cache(None)
        def f(n):
            ans = n
            for i in range(1, n):
                ans = max(ans, i * f(n - i))
            return ans

        ans = 1
        for i in range(1, n):
            ans = max(ans, i * f(n - i))
        return ans
