#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(s):
    ss = s.split(',')
    ans = 0
    for s in ss:
        value = 0
        for c in s:
            value += ord(c)
            value = value * 17 % 256
        ans += value
    return ans


def main():
    # test = True
    test = False
    input_file = 'tmp.in' if test else 'input.txt'

    with open(input_file) as fh:
        for s in fh:
            s = s.strip()
            ans = solve(s)
            print(ans)


if __name__ == '__main__':
    main()
