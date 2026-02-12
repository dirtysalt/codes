#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(reports):
    for i in range(1, len(reports)):
        if i >= 2:
            s1 = reports[i - 1] - reports[i - 2]
            s2 = reports[i] - reports[i - 1]
            if s1 * s2 < 0:
                return 0
        d = reports[i] - reports[i - 1]
        if abs(d) == 0 or abs(d) > 3:
            return 0
    return 1


def main():
    input = 'tmp.in'
    ans = 0
    with open(input) as fh:
        for s in fh:
            s = s.strip()
            reports = [int(x) for x in s.split()]
            ans += solve(reports)
    print(ans)


if __name__ == '__main__':
    main()
