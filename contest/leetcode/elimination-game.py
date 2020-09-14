#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def lastRemaining(self, n: int) -> int:
        return lastRemaining(n)


def lastRemaining(n):
    def next_state(x, trailing, bits):
        bit = (x >> bits) & 1
        trailing = ((1 - bit) << bits) + trailing
        bits += 1
        return trailing, bits

    def smallest(trailing, bits):
        if trailing == 0:
            return (1 << bits) + trailing
        else:
            return trailing

    def largest(trailing, bits):
        if trailing <= n:
            x = (n - trailing) // (1 << bits) * (1 << bits)
            return x + trailing
        else:
            return 0  # you have to break.

    x, trailing, bits = 1, 0, 0
    while True:
        trailing, bits = next_state(x, trailing, bits)
        y = largest(trailing, bits)
        if y <= x:
            break
        x = y
        trailing, bits = next_state(x, trailing, bits)
        y = smallest(trailing, bits)
        if y >= x or y <= 0:
            break
        x = y
    return x


def run_test():
    cases = [
        (1, 1),
        (9, 6),
        (2, 2),
        (3, 2),
        (4, 2),
        (6, 4)
    ]
    ok = True
    for c in cases:
        n, exp = c
        res = lastRemaining(n)
        if res != exp:
            print('case {} failed'.format(c))
            ok = False
    if ok:
        print('All cases are ok!')


if __name__ == '__main__':
    run_test()
