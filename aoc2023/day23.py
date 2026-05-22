#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import sys

new_recursion_limit = 20000  # 设置为你想要的新深度
sys.setrecursionlimit(new_recursion_limit)


def solve(grid):
    n, m = len(grid), len(grid[0])
    print(n, m)

    src, dst = 0, 0
    for j in range(m):
        if grid[0][j] == '.': src = j
        if grid[-1][j] == '.': dst = j

    map = {'v': (1, 0), '^': (-1, 0), '>': (0, 1), '<': (0, -1)}
    visit = [[0] * m for _ in range(n)]

    def run_with_seed(seed):
        import random
        rnd = random.Random(seed)

        def dfs(x, y):
            if (x, y) == (n - 1, dst):
                return 0

            visit[x][y] = 1
            c = grid[x][y]
            if c in map:
                dxy = [map[c]]
            else:
                dxy = list(map.values())
            rnd.shuffle(dxy)

            res = 0
            for dx, dy in dxy:
                x2, y2 = x + dx, y + dy
                if 0 <= x2 < n and 0 <= y2 < m and grid[x2][y2] != '#' and visit[x2][y2] == 0:
                    r = dfs(x2, y2)
                    res = max(res, r + 1)

            visit[x][y] = 0
            return res

        return dfs(0, src)

    ans = 0
    for seed in range(0, 20):
        r = run_with_seed(seed)
        print(f'iteration {seed} = {r}')
        ans = max(ans, r)
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


if __name__ == '__main__':
    main()
