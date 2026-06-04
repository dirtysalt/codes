#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def solve(space):
    space = [int(x) for x in space]
    # print(space)
    buf = []
    idx = 0
    for i in range(len(space)):
        if i % 2 == 0:
            buf.extend([idx] * space[i])
            idx += 1
        else:
            buf.extend([-1] * space[i])

    i, j = 0, len(buf) - 1
    while True:
        while j >= 0 and buf[j] == -1:
            j -= 1
        while i < len(buf) and buf[i] != -1:
            i += 1
        if i >= j: break
        buf[i], buf[j] = buf[j], buf[i]
        i += 1
        j -= 1

    # print(buf)
    ans = 0
    for i in range(len(buf)):
        if buf[i] == -1: break
        ans += i * buf[i]
    return ans


def main():
    input = 'tmp.in'
    with open(input) as fh:
        for s in fh:
            s = s.strip()
            if not s: continue
            print(solve(s))


if __name__ == '__main__':
    main()
