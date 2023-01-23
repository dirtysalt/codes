#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
#
# class Solution:
#     def idealArrays(self, n: int, maxValue: int) -> int:
#         adj = [[] for _ in range(1 + maxValue)]
#         for i in range(1, maxValue + 1):
#             for j in range(i, maxValue + 1):
#                 if j % i == 0:
#                     adj[i].append(j)
#
#         dp = [[0] * (1 + maxValue) for _ in range(2)]
#         for i in range(1 + maxValue):
#             dp[0][i] = 1
#
#         now = 0
#         MOD = 10 ** 9 + 7
#         for _ in range(1, n):
#             for i in range(1 + maxValue):
#                 dp[1 - now][i] = 0
#             for i in range(1, maxValue + 1):
#                 for x in adj[i]:
#                     dp[1 - now][x] += dp[now][i]
#             now = 1 - now
#
#         ans = sum(dp[now]) % MOD
#         return ans

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        ks = [[] for _ in range(maxValue + 1)]
        for i in range(2, maxValue + 1):
            k, x = 2, i
            while k * k <= x:
                if x % k == 0:
                    c = 0
                    while x % k == 0:
                        c += 1
                        x //= k
                    ks[i].append(c)
                k += 1
            if x > 1:
                ks[i].append(1)

        MOD = 10 ** 9 + 7

        import functools
        @functools.lru_cache(maxsize=None)
        def comb(n, k):
            if k == 0: return 1
            if n == k: return 1
            return (comb(n - 1, k - 1) + comb(n - 1, k)) % MOD

        ans = 0
        for i in range(1, maxValue + 1):
            mul = 1
            for k in ks[i]:
                mul = mul * comb(n + k - 1, k)
                mul = mul % MOD
            ans += mul
            ans %= MOD
        return ans


true, false, null = True, False, None
cases = [
    (2, 5, 10),
    (5, 3, 11),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().idealArrays, cases)

if __name__ == '__main__':
    pass
