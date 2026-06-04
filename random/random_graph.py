#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import ghalton
import numpy as np

ghalton_gen = ghalton.Halton(inDim=2)
numpy_gen = np.random.RandomState()


def to_int(ps, n):
    unit = 1 / n
    pvts = [i * unit for i in range(1, n)]
    pvts[-1] = 1

    def fx(p):
        for i in range(len(pvts)):
            if p <= pvts[i]:
                return i

    return [fx(p) for p in ps]


def gen_halton_random(n, m, size):
    zs = ghalton_gen.get(size)
    xs = to_int([p[0] for p in zs], n)
    ys = to_int([p[1] for p in zs], m)
    return zip(xs, ys)


def gen_numpy_random(n, m, size):
    xs = numpy_gen.randint(0, n, size=size)
    ys = numpy_gen.randint(0, m, size=size)
    return zip(xs, ys)


def gen_points(fn, n, m, size):
    zs = fn(n, m, size)
    pts = set()
    for x, y in zs:
        pts.add((x, y))
    return pts


def write_graph(n, m, pts, path):
    with open(path, 'w') as fh:
        fh.write('P1\n{} {}\n'.format(n, m))
        for i in range(n):
            for j in range(m):
                v = 1 if (i, j) in pts else 0
                fh.write('%d ' % v)
            fh.write('\n')
        fh.write('\n')


N, M, SIZE = 256, 256, 4000

pts = gen_points(gen_numpy_random, N, M, SIZE)
write_graph(N, M, pts, 'numpy_random.pbm')

pts = gen_points(gen_halton_random, N, M, SIZE)
write_graph(N, M, pts, 'halton_random.pbm')
