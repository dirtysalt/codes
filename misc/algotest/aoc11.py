#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import pprint

TEXT = """8448854321
4447645251
6542573645
4725275268
6442514153
4515734868
5513676158
3257376185
2172424467
6775163586"""


#
# TEXT = """11111
# 19991
# 19191
# 19991
# 11111"""
#
# TEXT = """5483143223
# 2745854711
# 5264556173
# 6141336146
# 6357385478
# 4167524645
# 2176841721
# 6882881134
# 4846848554
# 5283751526"""


def parse_text(text):
    input = []
    for s in text.split('\n'):
        s = s.strip()
        if not s: continue
        input.append([int(x) for x in s])
    return input


def step(mat):
    n, m = len(mat), len(mat[0])
    done = set()
    queue = []
    for i in range(n):
        for j in range(m):
            mat[i][j] += 1
            if mat[i][j] > 9:
                queue.append((i, j))
    while queue:
        (i, j) = queue.pop()
        if (i, j) in done: continue
        mat[i][j] = 0
        done.add((i, j))
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m and (x, y) not in done:
                    mat[x][y] += 1
                    if mat[x][y] > 9:
                        queue.append((x, y))
    return len(done)


def part1():
    mat = parse_text(TEXT)
    print('===== part1 =====')
    ans = 0
    for _ in range(100):
        ans += step(mat)
    print(ans)

    pprint.pprint(mat)


def part2():
    mat = parse_text(TEXT)
    print('===== part2 =====')
    for i in range(1000):
        ans = step(mat)
        if ans == len(mat) * len(mat[0]):
            print(i + 1)
            pprint.pprint(mat)
            break


part1()
part2()

if __name__ == '__main__':
    pass
