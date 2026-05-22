#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def gcd(a, b):
    while True:
        c = a % b
        if c == 0:
            return b
        a, b = b, c


def solve(a, b):
    MOD = 10 ** 9 + 7
    # c = a + b
    # C(c, a) = c ! / (a! * b!)
    num, den = 1, 1
    for i in range(0, a):
        num *= (b + i + 1)
        den *= (i + 1)
        factor = gcd(num, den)
        num //= factor
        den //= factor
    res = (num // den) % MOD
    return res


# print(solve(500, 500))


t = int(input())
for _ in range(t):
    a, b = input().rstrip().split()
    a, b = int(a), int(b)
    print((solve(a, b)))
