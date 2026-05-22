#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(grid):
    n, m = len(grid), len(grid[0])

    def ok(r, a, b):
        f, t = max(a - 1, 0), min(b + 1, m)
        for i in (r - 1, r, r + 1):
            if 0 <= i < n:
                for j in range(f, t):
                    if not grid[i][j].isdigit() and grid[i][j] != '.':
                        return True
        return False

    print(grid)
    ans = 0
    for i in range(n):
        # parse digits positions.
        pos = []
        start = -1
        for j in range(m):
            c = grid[i][j]
            if c.isdigit():
                if start == -1:
                    start = j
            else:
                if start != -1:
                    pos.append((start, j))
                    start = -1
        if start != -1:
            pos.append((start, m))

        # check each digits is adjacent to symbol.
        print(i, pos)
        for a, b in pos:
            if ok(i, a, b):
                x = int(grid[i][a:b])
                ans += x
    return ans


def main():
    # test = True
    test = False
    input_file = 'tmp.in' if test else 'input.txt'

    grid = []
    with open(input_file) as fh:
        for s in fh:
            s = s.strip()
            grid.append(s)
    ans = solve(grid)
    print(ans)
    return ans


if __name__ == '__main__':
    main()
