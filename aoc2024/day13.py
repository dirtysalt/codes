#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(x0, y0, x1, y1, x, y):
    # print(x0, y0, x1, y1, x, y)
    res = 1 << 30
    for i in range(100 + 1):
        for j in range(100 + 1):
            if ((x0 * i + x1 * j) == x) and ((y0 * i + y1 * j) == y):
                res = min(res, 3 * i + j)
    if res == (1 << 30): res = 0
    return res


def main():
    input = 'tmp.in'
    x0, y0, x1, y1, x, y = [1, 1, 1, 1, 1, 1]
    ans = 0
    with open(input) as fh:
        for s in fh:
            s = s.strip()
            if not s: continue
            a, b = s.split(': ')
            bs = b.split(', ')
            if a.endswith('A'):
                x0, y0 = int(bs[0][2:]), int(bs[1][2:])
            if a.endswith('B'):
                x1, y1 = int(bs[0][2:]), int(bs[1][2:])
            if a.endswith('Prize'):
                x, y = int(bs[0][2:]), int(bs[1][2:])
                r = solve(x0, y0, x1, y1, x, y)
                # print(r)
                ans += r
    print(ans)


if __name__ == '__main__':
    main()
