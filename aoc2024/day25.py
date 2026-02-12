#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def parse(grid):
    n, m = len(grid), len(grid[0])
    type = 0
    hs = []
    if all((x == '#' for x in grid[0])):
        type = 0
        for j in range(m):
            cnt = 0
            for i in range(1, n):
                if grid[i][j] == '#':
                    cnt += 1
                else:
                    break
            hs.append(cnt)
    else:
        type = 1
        for j in range(m):
            cnt = 0
            for i in reversed(range(n - 1)):
                if grid[i][j] == '#':
                    cnt += 1
                else:
                    break
            hs.append(cnt)
    return type, hs


def main():
    # input = 'debug.in'
    input = 'tmp.in'
    grid = []
    data = [[], []]
    with open(input) as fh:
        for s in fh:
            s = s.strip()
            if not s: continue
            grid.append(s)
            if len(grid) == 7:
                type, hs = parse(grid)
                data[type].append(hs)
                grid.clear()

    ans = 0
    keys, locks = data[0], data[1]
    # print(keys, locks)
    for k in keys:
        for l in locks:
            ok = True
            for i in range(len(k)):
                if k[i] + l[i] >= 6:
                    ok = False
                    break
            if ok:
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()
