#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(grid):
    for g in grid: print(g)
    n, m = len(grid), len(grid[0])
    cnt = [0] * (n + 1)
    for j in range(m):
        c = 0
        for i in reversed(range(n)):
            x = grid[i][j]
            if x == '#':
                for k in range(c):
                    cnt[i + 1 + k] += 1
                c = 0
            elif x == '.':
                pass
            else:
                c += 1

        for k in range(c):
            cnt[k] += 1

        print(cnt)

    print(cnt)
    ans = 0
    for i in range(n):
        ans += cnt[i] * (n - i)
    return ans


def main():
    # test = True
    test = False
    input_file = 'tmp.in' if test else 'input.txt'

    ans = []
    with open(input_file) as fh:
        grid = []
        for s in fh:
            s = s.strip()
            grid.append(s)
    ans = solve(grid)
    print(ans)


if __name__ == '__main__':
    main()
