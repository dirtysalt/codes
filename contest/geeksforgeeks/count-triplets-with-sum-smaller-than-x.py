#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(xs, x):
    xs.sort()
    n = len(xs)
    res = 0
    for i in range(0, n - 2):
        k = n - 1
        for j in range(i + 1, n - 1):
            while (xs[i] + xs[j] + xs[k]) >= x and (k > j):
                k -= 1
            if (k < j):
                break
            res += (k - j)
    return res


t = int(input())
for _ in range(t):
    s = input()
    n, x = [int(z) for z in s.rstrip().split()]
    xs = [int(z) for z in input().rstrip().split()]
    print(solve(xs, x))
