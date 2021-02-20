#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


MOD = 998244353


def pow(a, x):
    ans = 1
    while x > 0:
        if x % 2 == 1:
            ans = (ans * a) % MOD
        a = (a * a) % MOD
        x = x // 2
    return ans


def run(n, k):
    fac = [1] * (n + 1)
    for i in range(1, n + 1):
        fac[i] = (fac[i - 1] * i) % MOD

    ans = 0
    for a0 in range(1, n + 1):
        nn = n // a0 - 1
        if (nn - k + 1) < 0: break
        a = fac[nn]
        b = fac[k - 1]
        c = fac[nn - k + 1]
        d = (b * c) % MOD
        e = pow(d, MOD - 2)
        f = (a * e) % MOD
        ans = (ans + f) % MOD

    return ans


# this is codeforces main function
def main():
    from sys import stdin

    def read_int():
        return int(stdin.readline())

    def read_int_array(sep=None):
        return [int(x) for x in stdin.readline().split(sep)]

    def read_str_array(sep=None):
        return [x.strip() for x in stdin.readline().split(sep)]

    import os

    if os.path.exists('tmp.in'):
        stdin = open('tmp.in')

    n, k = read_int_array()
    ans = run(n, k)
    print(ans)


if __name__ == '__main__':
    main()
