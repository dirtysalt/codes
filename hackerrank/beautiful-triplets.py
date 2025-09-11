#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import sys

fh = sys.stdin

(n, d) = list(map(int, fh.readline().split(' ')))
arr = list(map(int, fh.readline().split(' ')))


def bs(arr, x):
    s = 0
    e = len(arr) - 1
    while s <= e:
        m = (s + e) / 2
        if arr[m] > x:
            e = m - 1
        elif arr[m] < x:
            s = m + 1
        else:
            return True
    return False


cnt = 0
for i in range(n):
    if bs(arr[i + 1:], arr[i] + d) and \
            bs(arr[i + 1:], arr[i] + 2 * d):
        cnt += 1
print(cnt)
