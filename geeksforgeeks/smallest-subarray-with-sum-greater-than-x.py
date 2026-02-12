#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def solve(xs, X):
    # print('input >', xs, X)
    n = len(xs)
    s, e = 0, 0
    res = n
    current = 0
    while True:
        while e < n and current <= X:
            current += xs[e]
            e += 1
        if current <= X:
            break
        # ok with e-1

        while current > X:
            current -= xs[s]
            s += 1

        # now current <= X and xs[s-1: e-1] > X
        # print(sum(xs[s - 1:e]), X)
        res = min(res, (e - s + 1))
    return res


t = int(input())
for _ in range(t):
    n, X = [int(x) for x in input().rstrip().split()]
    xs = [int(x) for x in input().rstrip().split()]
    print(solve(xs, X))
