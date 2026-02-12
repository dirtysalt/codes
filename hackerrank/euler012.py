#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def prime_build_table(n):
    table = [1] * (n + 1)
    table[1] = 0
    n2 = prime_upper_bound(n)
    for i in range(2, n2):
        if table[i] == 0:
            continue
        for j in range(2, n // i + 1):
            table[i * j] = 0
    return table


def prime_upper_bound(n):
    return min(n - 1, round(n ** 0.5) + 2)


PN = 10 ** 6
prime_table = prime_build_table(PN)
primes = [idx for idx in range(1, PN + 1) if prime_table[idx]]


# print('# of primes = {}'.format(len(primes)))


def solve(v):
    res = 1
    for p in primes:
        c = 1
        while v % p == 0:
            c += 1
            v = v // p
        res *= c
        if v == 1:
            break
    return res


N = 10 ** 3
idx = 1
n = 1
tables = [0] * (N + 1)
while True:
    v = idx * (idx + 1) // 2
    idx += 1
    res = solve(v)
    # print('solve({}) = {}'.format(v, res))
    while n < res and n <= N:
        tables[n] = v
        n += 1
    if n > N:
        break

cases = int(input())
for _ in range(cases):
    n = int(input())
    print((tables[n]))
