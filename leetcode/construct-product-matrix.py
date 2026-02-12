#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


def pow_mod(a, b, MOD):
    res = 1
    while b:
        if b & 0x1:
            res = (res * a) % MOD
        a = (a * a) % MOD
        b = b >> 1
    return res


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return d, x, y


# 相比费马小定理，这里不要求MOD是质数，只需要确保b和MOD是互质就行
# b * x + MOD * y =  1(% MOD)
def mod_inverse(b, MOD):
    d, x, y = extended_gcd(b, MOD)
    assert (d == 1)
    return x % MOD


class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        # 12345 = 3,5,823
        MOD = 12345
        A, B, C, D = 0, 0, 0, 1
        encode = {}
        for i in range(n):
            for j in range(m):
                a, b, c = 0, 0, 0
                x = grid[i][j]
                while x % 3 == 0:
                    a += 1
                    x = x // 3
                while x % 5 == 0:
                    b += 1
                    x = x // 5
                while x % 823 == 0:
                    c += 1
                    x = x // 823
                encode[(i, j)] = (a, b, c, x)
                A, B, C = A + a, B + b, C + c
                D = (D * x) % MOD

        # print(A, B, C, D)
        ans = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                a, b, c, d = encode[(i, j)]
                # (D/d) % MOD
                # D % MOD * (d^(-1) % MOD)
                v = D * mod_inverse(d, MOD)
                v = (v * pow_mod(3, (A - a), MOD)) % MOD
                v = (v * pow_mod(5, (B - b), MOD)) % MOD
                v = (v * pow_mod(823, (C - c), MOD)) % MOD
                ans[i][j] = v
        return ans


class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        ans = [[0] * m for _ in range(n)]
        prev = 1
        MOD = 12345
        for i in range(n):
            for j in range(m):
                ans[i][j] = prev
                prev = prev * grid[i][j]
                prev = prev % MOD
        prev = 1
        for i in reversed(range(n)):
            for j in reversed(range(m)):
                ans[i][j] = (ans[i][j] * prev) % MOD
                prev = prev * grid[i][j]
                prev = prev % MOD
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([[1, 2], [3, 4]], [[24, 12], [8, 6]]),
    ([[12345], [2], [1]], [[2], [0], [0]]),
    ([[3, 1, 1], [1, 3, 4]], [[12, 36, 36], [36, 12, 9]]),
]

aatest_helper.run_test_cases(Solution().constructProductMatrix, cases)

if __name__ == '__main__':
    pass
