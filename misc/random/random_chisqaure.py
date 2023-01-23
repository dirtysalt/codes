#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from collections import Counter

import ghalton
import numpy as np

gahlton_gen = ghalton.Halton(1)
numpy_gen = np.random.RandomState()


def gen_numpy_random(low, high, size):
    xs = numpy_gen.randint(low, high, size=size)
    return xs


def gen_halton_random(low, high, size):
    unit = 1 / (high - low)
    pvts = [i * unit for i in range(1, high - low + 1)]
    pvts[-1] = 1

    def to_int(p):
        for i in range(len(pvts)):
            if p <= pvts[i]:
                return i

    xs = gahlton_gen.get(size)
    ys = [to_int(p[0]) for p in xs]
    return ys


def compute_x2(fn, deg, size):
    n = deg + 1
    xs = fn(0, n, size)
    counter = Counter(xs)
    res = 0
    for k in range(n):
        v = counter[k]
        res += v * v
    return res * n / size - size


def test():
    deg, size = 5, 4000
    tests = 10
    print('degree = {}, size = {}'.format(deg, size))

    print('===== numpy random =====')
    xs = []
    for i in range(tests):
        x2 = compute_x2(gen_numpy_random, deg, size)
        xs.append(round(x2, 4))
    xs.sort()
    print(xs)

    print('===== halton random =====')
    xs = []
    for i in range(tests):
        x2 = compute_x2(gen_halton_random, deg, size)
        xs.append(round(x2, 4))
    xs.sort()
    print(xs)


test()
