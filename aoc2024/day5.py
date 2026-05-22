#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def solve(orders, sequences):
    lookup = {(x, y) for (x, y) in orders}

    def good(seq):
        for i in range(1, len(seq)):
            x, y = seq[i - 1], seq[i]
            if (x, y) not in lookup:
                return False
        return True

    ans = 0
    for seq in sequences:
        if good(seq):
            ans += seq[len(seq) // 2]
    return ans


def main():
    input = 'tmp.in'
    orders = []
    sequences = []
    with open(input) as fh:
        for s in fh:
            s = s.strip()
            if not s: break
            orders.append([int(x) for x in s.split('|')])

        for s in fh:
            sequences.append([int(x) for x in s.split(',')])

    print(solve(orders, sequences))


if __name__ == '__main__':
    main()
