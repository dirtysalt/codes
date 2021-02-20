#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from sys import stdin


def run(n, m, k):
    avg = n // k
    if m <= avg:
        return m

    a = avg
    b = m - avg
    c = (b + k - 2) // (k - 1)
    return a - c


def main():
    t = int(stdin.readline())
    for _ in range(t):
        n, m, k = [int(x) for x in stdin.readline().split()]
        ans = run(n, m, k)
        print(ans)


if __name__ == '__main__':
    import os

    if os.path.exists('tmp.in'):
        stdin = open('tmp.in')
    main()
