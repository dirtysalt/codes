#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def transpose(x):
    n, m = len(x), len(x[0])
    res = [[' '] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            res[j][i] = x[i][j]
    res = [''.join(x) for x in res]
    return res


def solve(grid):
    if not grid: return 0, 0

    def f(g):
        n = len(g)
        r = 0
        pos = []
        while r < n - 1:
            i, j = r, r + 1
            ok = True
            while i >= 0 and j < n:
                if g[i] != g[j]:
                    ok = False
                    break
                i -= 1
                j += 1
            if ok:
                pos.append(r + 1)
            r += 1
        # 不太理解意思，所以这里只能查找每个切分点
        # 最后发现每个case的确只有唯一一个切分点
        if not pos: pos = [0]
        return pos

    a = f(grid)
    grid2 = transpose(grid)
    b = f(grid2)
    return a[0], b[0]


def main():
    # test = True
    test = False
    input_file = 'tmp.in' if test else 'input.txt'

    ans = []
    with open(input_file) as fh:
        grid = []
        for s in fh:
            s = s.strip()
            if not s:
                ans.append(solve(grid))
                grid = []
            else:
                grid.append(s)
        ans.append(solve(grid))

    r, c = 0, 0
    for a, b in ans:
        r += a
        c += b
    ans = r * 100 + c
    print(r, c, ans)


if __name__ == '__main__':
    main()
