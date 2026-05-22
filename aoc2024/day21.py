#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import functools
import string


class PathFinder:
    def __init__(self, grid):
        self.grid = grid
        self.init()

    def find_path(self, ax, ay, bx, by, dx, dy):
        grid = self.grid
        n, m = len(grid), len(grid[0])
        from collections import deque
        q = deque()
        q.append(('', ax, ay))
        path = []
        while q:
            p, ax, ay = q.popleft()
            if ax == bx and ay == by:
                path.append(p)
                continue

            if ax != bx and grid[ax + dx][ay] != '#':
                r = ('v' if dx == 1 else '^')
                q.append((p + r, ax + dx, ay))

            if ay != by and grid[ax][ay + dy] != '#':
                r = ('>' if dy == 1 else '<')
                q.append((p + r, ax, ay + dy))
        return path

    def init(self):
        grid = self.grid
        n, m = len(grid), len(grid[0])
        pos = {}
        for i in range(n):
            for j in range(m):
                pos[grid[i][j]] = (i, j)

        @functools.cache
        def find_char(a, b):
            ax, ay = pos[a]
            bx, by = pos[b]
            dx = -1
            if ax < bx:
                dx = 1
            dy = -1
            if ay < by:
                dy = 1
            path = self.find_path(ax, ay, bx, by, dx, dy)
            return path

        self.find_char = find_char

    def find_seq(self, seq):
        seq = 'A' + seq
        find_char = self.find_char
        res = set([''])
        for i in range(1, len(seq)):
            a, b = seq[i - 1], seq[i]
            rs = find_char(a, b)
            new_res = []
            for old in res:
                for r in rs:
                    new_res.append(old + r + 'A')
            res = new_res
        return res


pf1 = PathFinder(['789', '456', '123', '#0A'])
pf2 = PathFinder(['#^A', '<v>'])
seq = pf1.find_seq('029A')
assert '<A^A>^^AvvvA' in seq
seq = pf2.find_seq('<A^A>^^AvvvA')
assert 'v<<A>>^A<A>AvA<^AA>A<vAAA>^A' in seq
seq = pf2.find_seq('v<<A>>^A<A>AvA<^AA>A<vAAA>^A')
assert '<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A' in seq


def solve(s):
    res = pf1.find_seq(s)

    res2 = set()
    for r in res:
        res2.update(pf2.find_seq(r))

    res3 = set()
    for r in res2:
        res3.update(pf2.find_seq(r))

    length = min([len(x) for x in res3])
    base = 0
    for c in s:
        if c in string.digits:
            base = base * 10 + int(c)
        else:
            break
    print(length, base)
    return length * base


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
