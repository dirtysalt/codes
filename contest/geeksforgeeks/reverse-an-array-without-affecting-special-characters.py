#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import string


def solve(s):
    s = list(s)
    tmp = [(idx, c) for (idx, c) in enumerate(s) if c in string.ascii_letters]
    b, e = 0, len(tmp) - 1
    while b < e:
        (bi, bc) = tmp[b]
        (ei, ec) = tmp[e]
        s[ei] = bc
        s[bi] = ec
        b += 1
        e -= 1
    return ''.join(s)


t = int(input())
for _ in range(t):
    s = input().rstrip()
    print(solve(s))
