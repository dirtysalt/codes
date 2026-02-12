#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(t, d):
    r = 0
    for t0 in range(1, t):
        if t0 * (t - t0) > d:
            r += 1
    return r


def main():
    # test = True
    test = False
    input_file = 'tmp.in' if test else 'input.txt'

    times = []
    dists = []
    with open(input_file) as fh:
        s = next(fh).strip()
        times = [int(x) for x in s.split(': ')[1].split()]
        s = next(fh).strip()
        dists = [int(x) for x in s.split(': ')[1].split()]

    ans = 1
    for t, d in zip(times, dists):
        r = solve(t, d)
        ans = ans * r

    print(ans)
    return ans


if __name__ == '__main__':
    main()
