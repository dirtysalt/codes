#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import os.path
from typing import List


class Solution:
    def ballGame(self, num: int, plate: List[str]) -> List[List[int]]:
        n, m = len(plate), len(plate[0])
        from collections import deque
        dq = deque()

        visit = [[[0] * 4 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if plate[i][j] == 'O':
                    for k in range(4):
                        dq.append((i, j, k, 0))
                        visit[i][j][k] = 1

        def direct(i, j, k):
            if plate[i][j] in 'O.':
                pass
            elif plate[i][j] == 'E':
                k = (k + 3) % 4
            elif plate[i][j] == 'W':
                k = (k + 1) % 4
            return k

        dxy = ((0, 1), (1, 0), (0, -1), (-1, 0))
        while dq:
            i, j, k, d = dq.popleft()
            if d >= num: continue
            dx, dy = dxy[k]
            i2, j2 = i - dx, j - dy
            if (d + 1) <= num and 0 <= i2 < n and 0 <= j2 < m:
                k = direct(i2, j2, k)
                if visit[i2][j2][k] == 0:
                    # if (i2, j2, k) not in visit:
                    #     visit.add((i2, j2, k))
                    visit[i2][j2][k] = 1
                    dq.append((i2, j2, k, d + 1))

        ans = []
        st = []
        st.extend([(0, j, 1) for j in range(1, m - 1)])
        st.extend([(n - 1, j, 3) for j in range(1, m - 1)])
        st.extend([(i, 0, 0) for i in range(1, n - 1)])
        st.extend([(i, m - 1, 2) for i in range(1, n - 1)])
        for i, j, k in st:
            if plate[i][j] == '.' and visit[i][j][k]:
                ans.append([i, j])
        ans.sort()
        return ans


class Solution:
    def ballGame(self, num: int, plate: List[str]) -> List[List[int]]:
        n, m = len(plate), len(plate[0])
        INF = 1 << 30
        dxy = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def direct(i, j, k):
            if plate[i][j] in 'O.':
                pass
            elif plate[i][j] == 'E':
                k = (k + 1) % 4
            elif plate[i][j] == 'W':
                k = (k + 3) % 4
            return k

        cache = [[[-1] * 4 for _ in range(m)] for _ in range(n)]

        def dfs(i, j, k):
            if i < 0 or i >= n or j < 0 or j >= m:
                return INF
            if plate[i][j] == 'O':
                return 0

            if cache[i][j][k] != -1:
                return cache[i][j][k]

            cache[i][j][k] = INF
            k2 = direct(i, j, k)
            dx, dy = dxy[k2]
            i2, j2 = i + dx, j + dy
            ret = dfs(i2, j2, k2)

            if ret != INF: ret += 1
            cache[i][j][k] = ret
            return ret

        st = []
        st.extend([(0, j, 1) for j in range(1, m - 1)])
        st.extend([(n - 1, j, 3) for j in range(1, m - 1)])
        st.extend([(i, 0, 0) for i in range(1, n - 1)])
        st.extend([(i, m - 1, 2) for i in range(1, n - 1)])
        ans = []
        for i, j, k in st:
            if plate[i][j] == '.':
                d = dfs(i, j, k)
                if d <= num:
                    ans.append([i, j])
        ans.sort()
        return ans


true, false, null = True, False, None
cases = [
    (4, ["..E.", ".EOW", "..W."], [[2, 1]]),
    (5, [".....", "..E..", ".WO..", "....."], [[0, 1], [1, 0], [2, 4], [3, 2]]),
    (3, [".....", "....O", "....O", "....."], []),
    (69,
     ["W.W.WE..", ".WWWEW..", "EWW.WE.E", "E.W.E.E.", ".OEOO.EO", "WE.WOE.W", "WW...E..", ".WEWO..O", "E....E..",
      ".OWE...."],
     [[0, 3], [0, 6], [1, 7], [4, 0], [6, 7], [9, 4], [9, 6]]),
]

import aatest_helper

if os.path.exists('../tmp.in'):
    with open('../tmp.in') as fh:
        x = eval(fh.readline())
        maze = eval(fh.readline())
        cases.append((x, maze, aatest_helper.ANYTHING))

aatest_helper.run_test_cases(Solution().ballGame, cases)

if __name__ == '__main__':
    pass
