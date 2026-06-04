#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(robots):
    n, m = 0, 0
    for x, y, _, _ in robots:
        m = max(m, x)
        n = max(n, y)
    n, m = n + 1, m + 1
    step = 100

    def f(robot):
        x, y, dx, dy = robot
        x = (x + dx * step) % m
        x = (x + m) % m
        y = (y + dy * step) % n
        y = (y + n) % n
        # print(robot, x, y)
        if x == (m // 2) or y == (n // 2):
            return -1
        a = (x < (m // 2))
        b = (y < (n // 2))
        return a * 2 + b

    cnt = [0] * 4
    for r in robots:
        d = f(r)
        if d == -1: continue
        cnt[d] += 1

    ans = 1
    for x in cnt:
        ans = ans * x
    return ans


def main():
    input = 'tmp.in'
    robots = []
    with open(input) as fh:
        for s in fh:
            s = s.strip()
            if not s: continue
            p, v = s.split()
            x, y = [int(x) for x in p[2:].split(',')]
            dx, dy = [int(x) for x in v[2:].split(',')]
            robots.append((x, y, dx, dy))
    print(solve(robots))


if __name__ == '__main__':
    main()
