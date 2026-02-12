#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def solve(values):
    final = []
    res = 0
    for p in range(50):
        for v in values:
            res += ord(v[p]) - ord('0')
        final.append(res % 10)
        res = res // 10
    while res:
        final.append(res % 10)
        res = res // 10
    final = [chr(ord('0') + x) for x in final]
    res = ''.join(final[-10:][::-1])
    return res


cases = int(input())
values = []
for _ in range(cases):
    values.append(input().rstrip()[::-1])
print((solve(values)))
