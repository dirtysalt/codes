#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from sys import stdin


# FIXME: WA
def run(h, c, t):
    a = h - t
    b = t - c
    if a == 0 or b == 0:
        return 1
    # print(a, b)

    if a % b == 0:
        return 1 + a // b
    if b % a == 0:
        return 1 + b // a

    # ax + by = gcd(x, y)

    def ext_gcd(a, b):
        if b == 0:
            return a, 1, 0
        d, x2, y2 = ext_gcd(b, a % b)
        x1, y1 = y2, x2 - (a // b) * y2
        return d, x1, y1

    d, x, y = ext_gcd(a, b)
    ans = abs(x) + abs(y)
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
