#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import random


def run_once(t=12):
    mask = [0] * t
    days = 0
    left = t
    while left > 0:
        x = random.randint(0, t - 1)
        if mask[x] == 0:
            mask[x] = 1
            left -= 1

        days += 1
    return days


def do_simulation():
    t = 12
    T = 10000
    ans = []

    for _ in range(T):
        days = run_once(t)
        ans.append(days)
    print('avg = %.2f' % (sum(ans) / len(ans)))


do_simulation()

if __name__ == '__main__':
    pass
