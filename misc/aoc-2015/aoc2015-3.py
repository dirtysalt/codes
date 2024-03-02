#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(s):
    i, j = 0, 0
    visit = set()
    map = {'^': (-1, 0), 'v': (1, 0), '>': (0, 1), '<': (0, -1)}
    visit.add((i, j))
    for c in s:
        dx, dy = map[c]
        i, j = i + dx, j + dy
        visit.add((i, j))
    return len(visit)


def main():
    # test = True
    test = False
    input_file = 'input.txt' if not test else 'tmp.in'

    ans = 0
    with open(input_file) as fh:
        for s in fh:
            s = s.strip()
            r = solve(s)
            print(s, '--->', r)
            ans += r

    print(ans)


if __name__ == '__main__':
    main()
