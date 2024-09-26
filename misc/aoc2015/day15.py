#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def solve(a, b, c, n):
    rep = n // (b + c)
    rem = n % (b + c)
    ans = a * b * rep + a * min(rem, b)
    return ans


def main():
    # test = True
    test = False
    input_file = 'input.txt' if not test else 'tmp.in'
    N = 1000 if test else 2503

    ans = 0
    with open(input_file) as fh:
        for s in fh:
            s = s.strip()
            ss = s.split()
            a, b, c = int(ss[3]), int(ss[6]), int(ss[13])
            r = solve(a, b, c, N)
            ans = max(ans, r)

    print(ans)


if __name__ == '__main__':
    main()
