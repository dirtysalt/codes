#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from sys import stdin


def run(h, c, t):
    if (h + c - 2 * t) >= 0:
        return 2

    a = h - t
    b = 2 * t - h - c
    k = int(a / b)
    val1 = abs((k + 1) * h + k * c - (2 * k + 1) * t)
    val2 = abs((k + 2) * h + (k + 1) * c - (2 * k + 3) * t)
    # val1 / (2k+1) <= val2 / (2k+3), return 2k+1
    if val1 * (2 * k + 3) <= val2 * (2 * k + 1):
        ans = 2 * k + 1
    else:
        ans = 2 * k + 3
    return ans


def main():
    cases = int(stdin.readline())
    for _ in range(cases):
        h, c, t = [int(x) for x in stdin.readline().split()]
        ans = run(h, c, t)
        print(ans)


if __name__ == '__main__':
    import os

    if os.path.exists('tmp.in'):
        stdin = open('tmp.in')
    main()
