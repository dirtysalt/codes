#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from sys import stdin


def run(n, k, scores):
    ans = 0
    for x in scores:
        if x > 0 and x >= scores[k - 1]:
            ans += 1
    print(ans)


def main():
    n, k = [int(x) for x in stdin.readline().split()]
    scores = [int(x) for x in stdin.readline().split()]
    run(n, k, scores)


if __name__ == '__main__':
    import os

    if os.path.exists('tmp.in'):
        stdin = open('tmp.in')
    main()
