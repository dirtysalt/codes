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

        import functools
        @functools.lru_cache(None)
        def fun(i, x, y):
            if i == N:
                return 0
            a, b = cnt[i]
            ans = fun(i + 1, x, y)
            if a <= x and b <= y:
                res = fun(i + 1, x - a, y - b) + 1
                ans = max(ans, res)

            return ans

        ans = fun(0, m, n)
        return ans
