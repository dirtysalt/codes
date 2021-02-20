#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# use pypy3 please.

N = 5 * (10 ** 6)
tables = [0] * (N + 1)
lookup = dict()
tables[1] = 1

for n in range(2, N + 1):
    if tables[n]:
        continue
    # print('works on n = {}'.format(n))
    v = n
    paths = [v]
    while True:
        if v % 2 == 0:
            v = v // 2
        else:
            v = 3 * v + 1
        if v < len(tables) and tables[v]:
            break
        if v >= len(tables) and v in lookup:
            break
        paths.append(v)
    paths = paths[::-1]
    if v < len(tables):
        res = tables[v]
    else:
        res = lookup[v]
    for (idx, p) in enumerate(paths):
        if p < len(tables):
            tables[p] = idx + res + 1

starting = [0] * (N + 1)
starting[1] = 1
max_chain = 1
max_index = 1
for n in range(2, N + 1):
    if tables[n] >= max_chain:
        max_chain = tables[n]
        max_index = n
    starting[n] = max_index

# print('OK!!')
t = int(input())
for _ in range(t):
    n = int(input())
    print((starting[n]))
