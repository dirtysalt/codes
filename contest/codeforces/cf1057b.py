#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from sys import stdin


def run(rs):
    n = len(rs)
    ans = 0
    for i in range(n):
        acc = 0
        c = 0
        for j in range(i, n):
            c += 1
            acc += rs[j]
            if acc > c * 100:
                ans = max(ans, c)
    print(ans)


def main():
    _ = int(stdin.readline())
    rs = [int(x) for x in stdin.readline().split()]
    run(rs)


if __name__ == '__main__':
    import os

    if os.path.exists('tmp.in'):
        stdin = open('tmp.in')
    main()
