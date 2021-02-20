#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from sys import stdin


def run(w):
    sz = len(w)
    if sz > 10:
        w = '%s%d%s' % (w[0], sz - 2, w[-1])
    print(w)


def main():
    n = int(stdin.readline())
    for i in range(n):
        w = stdin.readline().strip()
        run(w)


if __name__ == '__main__':
    import os

    if os.path.exists('tmp.in'):
        stdin = open('tmp.in')
    main()
