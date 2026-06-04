#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def solve(numbers):
    # print(numbers)

    def run(x):
        for _ in range(2000):
            x ^= (x * 64)
            x %= 16777216
            x ^= (x // 32)
            x %= 16777216
            x ^= (x * 2048)
            x %= 16777216
        return x

    ans = 0
    for x in numbers:
        x = run(x)
        ans += x
    return ans


def main():
    # input = 'debug.in'
    input = 'tmp.in'
    orders = []
    with open(input) as fh:
        for s in fh:
            orders.append(int(s))
    print(solve(orders))


if __name__ == '__main__':
    main()
