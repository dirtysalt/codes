#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List

class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:

        # import functools
        # @functools.lru_cache(maxsize = None)
        # def DP(n, k):
        #     if (k == 0): return 1
        #     if (n == 1): return 1
        #     res = 0
        #     for k1 in range(0, k+1):
        #         res += DP(n-1, k-k1)
        #     return res

        N = max((x[0] for x in queries))
        DP = [[0] * (N+1) for _ in range(20)]
        DP = [[0] * 20 for _ in range(N+1)]
        DP[0] = [1] * 20
        DP[1] = [1] * 20

        for i in range(2, N+1):
            for k in range(0, 20):
                ans = 0
                for k1 in range(0, k+1):
                    ans += DP[i-1][k-k1]
                DP[i][k] = ans

        # print(DP[3][10])


        PMS = [0] * 101
        for i in range(2, 100):
            if PMS[i] == 1: continue
            for j in range(i, 100):
                if i * j >= 100: break
                PMS[i * j] = 1
        PS = []
        for i in range(2, 100):
            if PMS[i] == 0: PS.append(i)

        # print(PS)

        MOD = 10 ** 9 + 7
        def test(n, k):
            ans = 1
            for p in PS:
                if k % p == 0:
                    cnt = 0
                    while k % p == 0:
                        cnt += 1
                        k = k // p
                    res = DP[n][cnt]
                    # print(n, p, cnt, res)
                    ans = ans * res

            if k != 1:
                ans = ans * DP[n][1]
            ans = ans % MOD
            return ans


        ans = []
        for n, k in queries:
            res =  test(n, k)
            ans.append(res)
        return ans

import aatest_helper
cases = [
    ([[2,6],[5,1],[73,660]], [4,1,50734910]),
    ( [[1,1],[2,2],[3,3],[4,4],[5,5]], [1,2,3,10,5]),
    ([[373,196],[101,229],[466,109],[308,83],[296,432]], [865201973, 101, 466, 308, 411805778]),
]

aatest_helper.run_test_cases(Solution().waysToFillArray, cases)
