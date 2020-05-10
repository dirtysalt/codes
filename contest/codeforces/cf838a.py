#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from sys import stdin


def run(n, m, pixels):
    ans = 1 << 30

    acc = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            acc[i + 1][j + 1] = acc[i + 1][j] + int(pixels[i][j])
        for j in range(m):
            acc[i + 1][j + 1] += acc[i][j + 1]
    # print(acc)

    for k in range(2, max(n, m) + 1):
        r, c = (n + k - 1) // k, (m + k - 1) // k
        res = 0
        for i in range(r):
            for j in range(c):
                x, y = i * k, j * k
                x2, y2 = min(x + k - 1, n - 1), min(y + k - 1, m - 1)
                zero = acc[x2 + 1][y2 + 1] - acc[x][y2 + 1] - acc[x2 + 1][y] + acc[x][y]
                # print(x, y, k, zero, k * k - zero)
                res += min(zero, k * k - zero)
        # print(k, res)
        ans = min(ans, res)
    print(ans)


def main():
    n, m = [int(x) for x in stdin.readline().split()]
    pixels = []
    for i in range(n):
        pixels.append(stdin.readline().strip())
    run(n, m, pixels)


if __name__ == '__main__':
    import os

    if os.path.exists('tmp.in'):
        stdin = open('tmp.in')
    main()
