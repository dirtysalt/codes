#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def main():
    # test = True
    test = False
    input_file = 'tmp.in' if test else 'input.txt'

    inst = None
    network = {}
    with open(input_file) as fh:
        inst = next(fh).strip()
        for s in fh:
            s = s.strip()
            if not s: continue
            loc, s = s.split(' = ')
            s = s[1:-1]
            l, r = s.split(', ')
            network[loc] = (l, r)

    print(inst, network)
    now = 'AAA'
    i, ans = 0, 0
    while now != 'ZZZ':
        c = inst[i]
        ans += 1
        i = (i + 1) % len(inst)
        d = 1 if c == 'R' else 0
        now = network[now][d]
        # print(ans, now)

    print(ans)


if __name__ == '__main__':
    main()
