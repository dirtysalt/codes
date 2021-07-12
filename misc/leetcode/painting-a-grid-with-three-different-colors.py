#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        def single():
            states = []
            for x in range(3 ** m):
                st = []
                x2 = x
                for i in range(m):
                    st.append(x2 % 3)
                    x2 = x2 // 3
                ok = True
                for i in range(1, m):
                    if st[i] == st[i - 1]:
                        ok = False
                        break
                if ok:
                    states.append(x)
            return states

        states = single()

        def cross(x, y):
            st0 = states[x]
            st1 = states[y]
            for _ in range(m):
                if st0 % 3 == st1 % 3: return False
                st0 = st0 // 3
                st1 = st1 // 3
            return True

        N = len(states)
        dp = [[0] * N for _ in range(2)]
        for i in range(N):
            dp[0][i] = 1

        now = 0
        MOD = 10 ** 9 + 7
        # print(N)
        for _ in range(n - 1):
            for x in range(N):
                acc = 0
                for y in range(N):
                    if cross(x, y):
                        acc += dp[now][y]
                        acc = acc % MOD
                dp[1 - now][x] = acc
            now = 1 - now

        ans = sum(dp[now]) % MOD
        return ans


true, false, null = True, False, None
cases = [
    (1, 1, 3),
    (1, 2, 6),
    (5, 5, 580986),
    (5, 1000, 408208448)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().colorTheGrid, cases)

if __name__ == '__main__':
    pass
