#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def solve(N, M, G, S):
    a = M * G
    s, e = 0, N - 1
    cnt = 0
    while s <= e:
        m = (s + e) // 2
        cnt += 1
        if m == (M - 1):
            break
        elif m > (M - 1):
            e = m - 1
        else:
            s = m + 1
    b = cnt * S
    if a < b:
        return 1
    elif a > b:
        return 2
    return 0


t = int(input())
for _ in range(t):
    N, M, G, S = [int(x) for x in input().strip().split()]
    print(solve(N, M, G, S))
