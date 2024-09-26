#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(s):
    xs = [int(x) for x in s.split('x')]
    xs.sort()
    a, b, c = xs
    return 2 * (a * b + b * c + a * c) + a * b


def main():
    # test = True
    test = False
    input_file = 'input.txt' if not test else 'tmp.in'

    ans = 0
    with open(input_file) as fh:
        for s in fh:
            s = s.strip()
            r = solve(s)
            print(s, '--->', r)
            ans += r

    print(ans)


if __name__ == '__main__':
    main()
