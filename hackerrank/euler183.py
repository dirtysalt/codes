#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

N = 10 ** 6
dp = [0] * (N + 1)


def precompute():
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def guess(n):
        import math
        k = n // math.e
        if (k + 1) * math.log(n / (k + 1)) > k * math.log(n / k):
            k += 1

        _g = gcd(n, k)
        k = k // _g
        while k % 5 == 0: k = k // 5
        while k % 2 == 0: k = k // 2
        return k == 1

    for i in range(5, N + 1):
        term = guess(i)
        dp[i] = i if not term else -i
        dp[i] += dp[i - 1]


def run(n):
    ans = dp[n] - dp[4]
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

    precompute()
    # print(dp)
    q = read_int()
    for _ in range(q):
        n = read_int()
        ans = run(n)
        print(ans)


if __name__ == '__main__':
    main()
