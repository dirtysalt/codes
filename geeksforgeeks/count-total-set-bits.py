#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def solve(n):
    try_bit = 31
    res = 0
    while n > 1:
        try_value = 1 << try_bit
        if n < try_value:
            try_bit -= 1
            continue

        res += try_bit * try_value // 2
        res += (n - try_value + 1)
        n -= try_value
    res += n
    return res


t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))
