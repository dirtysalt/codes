#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from sys import stdin


def PR(x):
    print(x, end='')


def run(n, k):
    if n > (k - 1) and (n - k - 1) % 2 == 1:
        print('YES')
        PR('1 ' * (k - 1))
        print(str(n - k + 1))
        return

    if n > 2 * (k - 1) and (n - 2 * k + 2) % 2 == 0:
        print('YES')
        PR('2 ' * (k - 1))
        print(str(n - 2 * k + 2))
        return

    print('NO')


def main():
    t = int(stdin.readline())
    for _ in range(t):
        n, k = [int(x) for x in stdin.readline().split()]
        run(n, k)


if __name__ == '__main__':
    import os

    if os.path.exists('tmp.in'):
        stdin = open('tmp.in')
    main()
