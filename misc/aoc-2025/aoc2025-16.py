#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(grid):
    n, m = len(grid), len(grid[0])
    for g in grid: print(g)
    visit = set()
    from collections import deque
    q = deque()
    direction = {
        'R': (0, 1),
        'L': (0, -1),
        'U': (-1, 0),
        'D': (1, 0),
    }

    q.append((0, -1, 'R'))
    while q:
        item = q.popleft()
        print(item)
        if item in visit: continue
        visit.add(item)
        x, y, d = item
        dx, dy = direction[d]
        x2, y2 = x + dx, y + dy
        if not (0 <= x2 < n and 0 <= y2 < m): continue

        c = grid[x2][y2]
        if c == '.':
            q.append((x2, y2, d))
        elif c == '/':
            for z in 'RU,LD,UR,DL'.split(','):
                if z[0] == d:
                    q.append((x2, y2, z[1]))
                    break
        elif c == '\\':
            for z in 'RD,LU,UL,DR'.split(','):
                if z[0] == d:
                    q.append((x2, y2, z[1]))
                    break
        elif c == '|':
            if d in 'UD':
                q.append((x2, y2, d))
            else:
                q.append((x2, y2, 'U'))
                q.append((x2, y2, 'D'))
        elif c == '-':
            if d in 'LR':
                q.append((x2, y2, d))
            else:
                q.append((x2, y2, 'L'))
                q.append((x2, y2, 'R'))
        else:
            raise Exception("unknown char: " + c)

    visit.remove((0, -1, 'R'))
    pos = set()
    for x, y, d in visit:
        pos.add((x, y))
    print(pos)
    return len(pos)


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
