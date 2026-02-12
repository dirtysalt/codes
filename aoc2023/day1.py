#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import string


def parse_input(s):
    ans = 0
    for c in s:
        if c in string.digits:
            ans += int(c) * 10
            break
    for c in s[::-1]:
        if c in string.digits:
            ans += int(c)
            break
    return ans


def main():
    # test = True
    test = False
    input_file = 'tmp.in' if test else 'input.txt'

    ans = 0
    with open(input_file) as fh:
        for s in fh:
            s = s.strip()
            r = parse_input(s)
            print(s, '---->', r)
            ans += r
    print('ans = ', ans)
    return ans


if __name__ == '__main__':
    main()
