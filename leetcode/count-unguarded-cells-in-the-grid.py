#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        M = [[0] * n for _ in range(m)]
        W = set()
        for i, j in walls:
            W.add((i, j))
            M[i][j] = 1
        visited = set()

        from collections import deque
        dq = deque()
        for i, j in guards:
            for k in range(4):
                dq.append((i, j, k))

        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        while dq:
            i, j, k = dq.popleft()
            if (i, j, k) in visited:
                continue
            visited.add((i, j, k))
            M[i][j] = 1
            i2, j2 = i + dirs[k][0], j + dirs[k][1]
            if 0 <= i2 < m and 0 <= j2 < n and (i2, j2) not in W:
                dq.append((i2, j2, k))

        ans = 0
        for i in range(m):
            for j in range(n):
                if M[i][j] == 0:
                    ans += 1
        return ans


if __name__ == '__main__':
    pass
