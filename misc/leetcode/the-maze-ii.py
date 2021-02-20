#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: the shortest distance for the ball to stop at the destination
    """

    def shortestDistance(self, maze, start, destination):
        # write your code here

        n = len(maze)
        m = len(maze[0])
        visited = [[0] * m for _ in range(n)]

        start = tuple(start)
        destination = tuple(destination)

        left_rolls = []
        right_rolls = []
        for i in range(n):
            xs = []
            p = -1
            for j in range(m):
                xs.append(p)
                if maze[i][j] == 1:
                    p = j
            left_rolls.append(xs[::])
            xs = []
            p = m
            for j in range(m - 1, -1, -1):
                xs.append(p)
                if maze[i][j] == 1:
                    p = j
            right_rolls.append(xs[::-1])

        up_rolls = []
        down_rolls = []
        for j in range(m):
            xs = []
            p = -1
            for i in range(n):
                xs.append(p)
                if maze[i][j] == 1:
                    p = i
            up_rolls.append(xs[::])
            xs = []
            p = n
            for i in range(n - 1, -1, -1):
                xs.append(p)
                if maze[i][j] == 1:
                    p = i
            down_rolls.append(xs[::-1])

        def dfs(r, c, direction):
            if (r, c) == destination:
                return 0
            visited[r][c] = 1
            next_rc = None
            if direction == 0:  # left.
                p = left_rolls[r][c]
                next_rc = r, p + 1
            elif direction == 1:  # right.
                p = right_rolls[r][c]
                next_rc = r, p - 1
            elif direction == 2:  # up.
                p = up_rolls[c][r]
                next_rc = p + 1, c
            else:  # down
                p = down_rolls[c][r]
                next_rc = p - 1, c

            res = -1
            if next_rc and next_rc != (r, c):
                r2, c2 = next_rc
                if 0 <= r2 < n and 0 <= c2 < m and maze[r2][c2] == 0 and visited[r2][c2] == 0:
                    delta = abs(r2 - r) + abs(c2 - c)
                    for d in range(4):
                        out = dfs(r2, c2, d)
                        if out != -1 and (res == -1 or res > (out + delta)):
                            res = out + delta
            visited[r][c] = 0
            return res

        r, c = start
        res = -1
        for d in range(0, 4):
            out = dfs(r, c, d)
            if out != -1 and (res == -1 or res > out):
                res = out
        return res
