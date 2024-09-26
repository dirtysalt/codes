#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(s):
    header, s = s.split(': ')
    a, b = s.split('|')
    wins = {int(x) for x in a.split()}
    have = {int(x) for x in b.split()}
    c = len(wins & have)
    return 1 << (c - 1) if c > 0 else 0


def main():
    # test = True
    test = False
    input_file = 'tmp.in' if test else 'input.txt'

    ans = 0
    with open(input_file) as fh:
        for s in fh:
            s = s.strip()
            r = solve(s)
            print(s, r)
            ans += r

    print(ans)


if __name__ == '__main__':
    main()
