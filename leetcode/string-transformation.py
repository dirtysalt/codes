#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def mat_mul(a, b, MOD):
    R, K, C = len(a), len(a[0]), len(b[0])
    res = [[0] * C for _ in range(R)]
    for k in range(K):
        for i in range(R):
            for j in range(C):
                res[i][j] += (a[i][k] * b[k][j]) % MOD
                res[i][j] %= MOD
    return res


def FindCutByKMP(s, t):
    n = len(s)
    def compute_max_match(pattern):
        match = [0] * len(pattern)
        c = 0
        for i in range(1, len(pattern)):
            v = pattern[i]
            while c and pattern[c] != v:
                c = match[c - 1]
            if pattern[c] == v:
                c += 1
            match[i] = c
        return match

    def kmp_search(text, pattern):
        match = compute_max_match(pattern)
        match_count = c = 0
        for i, v in enumerate(text):
            v = text[i]
            while c and pattern[c] != v:
                c = match[c - 1]
            if pattern[c] == v:
                c += 1
            if c == len(pattern):
                match_count += 1
                c = match[c - 1]
        return match_count

    cuts = kmp_search(s + s[:-1], t)
    return cuts


def ComputeMM(c, k, s, t):
    # f[i][0] after i operations, s == t
    # f[i][1] after i operations, s!= t

    # f[i][0] = f[i-1][0] * (c-1) + f[i-1][1] * c
    # f[i][1] = f[i-1][0] * (n-c) * f[i-1][1] * (n-1-c)

    # f[0][0] = 1 if s == t
    MOD = 10 ** 9 + 7
    n = len(s)
    base = [[c - 1, c], [n - c, n - 1 - c]]
    eq = 1 if (s == t) else 0
    T = [[eq], [1 - eq]]
    while k:
        if k & 0x1:
            T = mat_mul(base, T, MOD)
        base = mat_mul(base, base, MOD)
        k = k >> 1
    return T[0][0]


class Solution:
    def numberOfWays(self, s: str, t: str, k: int) -> int:
        cuts = FindCutByKMP(s, t)
        if cuts == 0: return 0
        return ComputeMM(cuts, k, s, t)


true, false, null = True, False, None

cases = [
    ("abcd", "cdab", 2, 2),
    ("ababab", "ababab", 1, 2),
    ("ceoceo", "eoceoc", 4, 208),
    ("ib", "ib", 10, 1),
    ("goxoq", "dfqgl", 244326024901249, 0),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().numberOfWays, cases)

if __name__ == '__main__':
    pass
