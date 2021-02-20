#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import numpy as np


def get_ceil_lgn(x):
    res = 0
    x -= 1
    while x:
        res += 1
        x >>= 1
    return res


def get_floor_lgn(x):
    res = get_ceil_lgn(x)
    if (1 << res) == x:
        return res
    return res - 1


# st[i][j] is index of min value in A[i..i+(1<<j)-1]
# st[i][j] = min index of (st[i][j-1], and st[i+(1<<j-1)][j-1])
# st[i][j-1] includes A[i..i+(1<<j-1)-1]
# and st[i+(1<<j-1)][j-1] includes A[i+(1<<j-1) .. i+(1<<j)-1]
def rmq_build_sparse_table(A):
    n = len(A)

    lgn = get_ceil_lgn(n)
    lgn += 1

    st = [[None] * lgn for _ in range(n)]
    for i in range(n):
        st[i][0] = i

    for j in range(1, lgn):
        for i in range(n):
            idx0 = st[i][j - 1]
            idx1 = None
            right = i + (1 << (j - 1))
            if right < n:
                idx1 = st[right][j - 1]

            if idx1 is None or A[idx0] <= A[idx1]:
                st[i][j] = idx0
            else:
                st[i][j] = idx1

    return st


# A[left.. left + (1 << lgn - 1] and A[right - (1<<lgn) + 1.. right]
# two intervals must be adjacent or overlapped.
def rmq_query(A, st, left, right):
    # [left..right] inclusive.
    lgn = get_floor_lgn(right - left + 1)
    idx0 = st[left][lgn]
    idx1 = st[right - (1 << lgn) + 1][lgn]
    if idx1 is None or A[idx0] < A[idx1]:
        return idx0
    return idx1


def bf_check(A, left, right):
    return np.argmin(A[left: right + 1]) + left


def main():
    for size in (1, 5, 10, 12, 16, 18, 20):
        A = np.random.random(size=size)
        st = rmq_build_sparse_table(A)
        for left in range(size):
            for right in range(left + 1, size):
                x = rmq_query(A, st, left, right)
                y = bf_check(A, left, right)
                if x != y:
                    print('F')
        print('PASS ON SIZE {}'.format(size))


if __name__ == '__main__':
    main()
