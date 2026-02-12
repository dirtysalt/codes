#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(grid, steps):
    n, m = len(grid), len(grid[0])
    x, y = 0, 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '@':
                x, y = i, j
                break

    def push(x, y, dx, dy):
        dot = 0
        obj = 0
        while grid[x][y] in '@O':
            obj += 1
            x, y = x + dx, y + dy

        while grid[x][y] == '.':
            dot += 1
            x, y = x + dx, y + dy
            # 这个条件有点那啥，即使先前有多个., 但是只能推进一次
            if dot == 1:
                break

        for _ in range(obj):
            x, y = x - dx, y - dy
            grid[x][y] = 'O'

        nx, ny = x, y
        grid[nx][ny] = '@'

        for _ in range(dot):
            x, y = x - dx, y - dy
            grid[x][y] = '.'
        return nx, ny

    dxy = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    for s in steps:
        dx, dy = dxy[s]
        nx, ny = x + dx, y + dy
        if grid[nx][ny] == 'O':
            nx, ny = push(x, y, dx, dy)
            if dx == 0: assert nx == x
            if dy == 0: assert ny == y
        elif grid[nx][ny] == '.':
            grid[nx][ny] = '@'
            grid[x][y] = '.'
        else:
            assert grid[nx][ny] == '#'
            nx, ny = x, y
        x, y = nx, ny
        # print('=========', s, x, y)
        # for g in grid:
        #     print(g)
        assert 0 <= nx < n and 0 <= ny < m

    ans = 0
    cnt = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'O':
                r = i * 100 + j
                cnt += 1
                ans += r
    # print(cnt)
    return ans


def main():
    input = 'tmp.in'
    grid = []
    steps = []
    with open(input) as fh:
        for s in fh:
            s = s.strip()
            if not s: break
            grid.append(list(s))
        for s in fh:
            s = s.strip()
            steps.append(s)
    # print(steps)
    print(solve(grid, ''.join(steps)))


if __name__ == '__main__':
    main()
