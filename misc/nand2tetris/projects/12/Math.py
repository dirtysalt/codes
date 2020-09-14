#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import math


def _div1(x, y):
    if x < y:
        return 0
    q = _div1(x, 2 * y)
    q2 = q * 2
    qy2 = q2 * y
    if (x - qy2) < y:
        pass
    else:
        q2 += 1
    return q2


def _div2(x, y):
    if x < y:
        return 0, 0
    q, qy2 = _div2(x, 2 * y)
    q2 = q * 2
    # qy2 = q * 2 * y = q2 * y
    if (x - qy2) < y:
        pass
    else:
        q2 += 1
        # 如果这里q2 += 1的话，那qy2需要+y
        qy2 += y
    return q2, qy2


def div(x, y):
    q1 = _div1(x, y)
    q2, _ = _div2(x, y)
    assert q1 == q2
    return q2


def mul(x, y):
    res = 0
    shift = x
    while y:
        if y & 0x1:
            res += shift
        y >>= 1
        shift <<= 1
    return res


def sqrt(x):
    v = 0
    for i in reversed(range(32)):
        t = v + (1 << i)
        if (t * t) <= x:
            v = t
    return v


for i in range(2, 7):
    assert div(10, i) == (10 // i)
    assert div(20, i) == (20 // i)

for i in range(0, 10):
    for j in range(0, 10):
        assert mul(i, j) == i * j

for i in range(0, 10000):
    assert sqrt(i) == int(math.sqrt(i))
