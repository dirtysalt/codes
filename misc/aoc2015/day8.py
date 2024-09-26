#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(s):
    a = eval(s)
    print(len(s), len(a))
    return len(s) - len(a)


def main():
    # test = True
    test = False
    input_file = 'input.txt' if not test else 'tmp.in'

    ans = 0
    with open(input_file) as fh:
        for s in fh:
            s = s.strip()
            r = solve(s)
            ans += r

    print(ans)


if __name__ == '__main__':
    main()
