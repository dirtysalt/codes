#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from collections import Counter


def solve(n, k, numbers):
    counter = Counter()
    res = []
    output = []
    for x in numbers:
        cnt = counter[x] + 1
        counter[x] += 1

        ok = False
        for i in range(len(res)):
            if res[i][0] == x:
                res[i] = (x, cnt)
                ok = True
                pos = i
                break

        if not ok:
            res.append((x, cnt))
            pos = len(res) - 1

        for i in range(pos, 0, -1):
            if res[i][1] > res[i - 1][1] or (res[i][1] == res[i - 1][1] and res[i][0] < res[i - 1][0]):
                res[i], res[i - 1] = res[i - 1], res[i]
            else:
                break

        if len(res) > k:
            res.pop()

        for x in res:
            output.append(x[0])
    # return output
    return ' '.join([str(x) for x in output])


t = int(input())
for _ in range(t):
    n, k = [int(x) for x in input().split()]
    numbers = [int(x) for x in input().split()]
    print(solve(n, k, numbers))
