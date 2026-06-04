#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(input):
    import re
    reg = re.compile(r'mul\((?P<num1>\d+),(?P<num2>\d+)\)')
    pos = 0
    ans = 0
    while pos < len(input):
        p = reg.search(input, pos=pos)
        if not p: break
        pos = p.span()[1]
        d = p.groupdict()
        a = int(d['num1'])
        b = int(d['num2'])
        ans += a * b
    return ans


def main():
    input = 'tmp.in'
    ans = 0
    with open(input) as fh:
        for s in fh:
            s = s.strip()
            ans += solve(s)
    print(ans)


if __name__ == '__main__':
    main()
