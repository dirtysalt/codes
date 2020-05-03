#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def solve(n):
    # even bits
    a = (n & 0x55555555) << 1
    # odd bits
    b = (n & 0xaaaaaaaa) >> 1
    return a | b


t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))
