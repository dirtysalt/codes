#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# !/bin/python3

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    ans = [0, 0]
    for d in apples:
        x = a + d
        if s <= x <= t:
            ans[0] += 1
    for d in oranges:
        x = b + d
        if s <= x <= t:
            ans[1] += 1
    for x in ans:
        print(x)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
