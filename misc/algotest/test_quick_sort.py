#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import numpy as np


# complex implementation.
# def qsort_pivot(xs, s, e):
#     pivot = xs[s]
#     a, b = s, e
#     while True:
#         while a < b and xs[b] > pivot:
#             b -= 1
#         if a == b:
#             break
#         xs[a] = xs[b]
#         a += 1
#         while a < b and xs[a] < pivot:
#             a += 1
#         if a == b:
#             break
#         xs[b] = xs[a]
#         b -= 1
#         if a == b:
#             break
#     assert a == b
#     xs[a] = pivot
#     return a


def qsort_pivot(xs, s, e):
    pivot = xs[e]
    slot = s
    for i in range(s, e):
        if xs[i] < pivot:
            xs[slot], xs[i] = xs[i], xs[slot]
            slot += 1
    xs[slot], xs[e] = xs[e], xs[slot]
    return slot


def qsort_range(xs, s, e):
    if s >= e:
        return
    p = qsort_pivot(xs, s, e)
    qsort_range(xs, s, p - 1)
    qsort_range(xs, p + 1, e)


def qsort(xs):
    n = len(xs)
    qsort_range(xs, 0, n - 1)


def check_qsort():
    print('check qsort ...')
    n = 10 ** 3
    t = 1000
    for _ in range(t):
        xs = np.random.randint(-10 ** 6, 10 ** 6, n)
        xs2 = xs.copy()
        qsort(xs)
        xs2.sort()
        assert np.all(np.array(xs) == xs2)
    print('PASSED!!!')


if __name__ == '__main__':
    check_qsort()
