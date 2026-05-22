#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:

        def dfs(i, prog):
            ans = 0
            if i == n:
                print(prog, y ** len(prog))
                return y ** len(prog)
            for j in range(x):
                prog[j] += 1
                ans += dfs(i + 1, prog)
                prog[j] -= 1
                if prog[j] == 0:
                    del prog[j]
            return ans

        # from collections import Counter
        # return dfs(0, Counter())

        # sum{i=0..x}(y ** i * C(x, i) * F(n, i))
        # F(n, i) 把n个人配置到i个项目里面，并且至少去确保每个都存在一个
        # F(n, i) = (i**n) - F(n,i-1)*C(i,i-1) - F(n,i-2)*C(i,i-2)....
        # F(n, 1) = 1
        MOD = 10 ** 9 + 7

        # a ^ b
        import functools

        @functools.lru_cache(None)
        def pow(a, b):
            ans = 1
            t = a
            while b:
                if b & 0x1:
                    ans = (ans * t) % MOD
                t = (t * t) % MOD
                b = b >> 1
            return ans

        C = [[0] * (x + 1) for _ in range(x + 1)]
        C[0][0] = 1
        for i in range(1, x + 1):
            for j in range(0, i + 1):
                C[i][j] = C[i - 1][j] + (C[i - 1][j - 1] if j > 0 else 0)
                C[i][j] %= MOD

        F = [0] * (x + 1)
        F[1] = 1
        for i in range(2, x + 1):
            acc = 0
            for j in reversed(range(i)):
                acc += (F[j] * C[i][j]) % MOD
                acc = acc % MOD
            F[i] = (pow(i, n) - acc) % MOD

        ans = 0
        for i in range(0, x + 1):
            r = pow(y, i) * C[x][i] * F[i]
            # print(i, r, '===>', pow(y, i), C[x][i], F[i])
            ans = (ans + r) % MOD
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    (1, 2, 3, 6),
    (5, 2, 1, 32),
    (3, 3, 4, 684),
    (4, 2, 1, 16),
]

aatest_helper.run_test_cases(Solution().numberOfWays, cases)

if __name__ == '__main__':
    pass
