#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import math


def run(pairs, k):
    xs = [(x[1] * math.log2(x[0]), x) for x in pairs]
    xs.sort()
    ans = xs[k - 1][1]
    return ans


# this is codeforces main function
def main():
    from sys import stdin

    def read_int():
        return int(stdin.readline())

    def read_int_array(sep=None):
        return [int(x) for x in stdin.readline().split(sep)]

    def read_str_array(sep=None):
        return [x.strip() for x in stdin.readline().split(sep)]

    import os

    if os.path.exists('tmp.in'):
        stdin = open('tmp.in')

    N = read_int()
    pairs = []
    for i in range(N):
        pairs.append(read_int_array())
    k = read_int()
    ans = run(pairs, k)
    print(' '.join(str(x) for x in ans))


if __name__ == '__main__':
    main()
