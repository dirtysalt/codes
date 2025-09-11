#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(a):
    n = len(a)
    for i in range(0, n - 1):
        if (i % 2 == 0 and a[i] > a[i + 1]) or (i % 2 == 1 and a[i] < a[i + 1]):
            a[i], a[i + 1] = a[i + 1], a[i]
    return ' '.join(map(str, a))


t = int(input())
for _ in range(t):
    n = int(input())
    xs = [int(x) for x in input().rstrip().split()]
    print(solve(xs))
