#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(s):
    ans = 0
    for c in s:
        if c == '(':
            ans += 1
        else:
            ans -= 1
    return ans


def main():
    # test = True
    test = False
    input_file = 'input.txt' if not test else 'tmp.in'

    with open(input_file) as fh:
        s = next(fh).strip()
        ans = solve(s)

    print(ans)


if __name__ == '__main__':
    main()
