#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimalSteps(self, maze: List[str]) -> int:
        inf = 1 << 30
        S, T = None, None
        MS, OS = [], []
        n, m = len(maze), len(maze[0])

        def bfs(s):
            from collections import deque
            nm = n * m
            depth = [inf] * nm
            dq = deque()
            depth[s] = 0
            dq.append(s)
            while dq:
                s = dq.popleft()
                d = depth[s]
                x, y = s // m, s % m
                for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                    x2, y2 = x + dx, y + dy
                    s2 = x2 * m + y2
                    if 0 <= x2 < n and 0 <= y2 < m and maze[x2][y2] != '#' and depth[s2] == inf:
                        depth[s2] = d + 1
                        dq.append(s2)
            return depth

        for i in range(n):
            for j in range(m):
                s = i * m + j
                c = maze[i][j]
                if c == 'S':
                    S = s
                elif c == 'T':
                    T = s
                elif c == 'M':
                    MS.append(s)
                elif c == 'O':
                    OS.append(s)

        # O((M+O) * S)
        D = {}
        D[S] = bfs(S)
        if D[S][T] == inf:
            return -1
        for M in MS:
            D[M] = bfs(M)
        if not MS:
            return D[S][T]
        for O in OS:
            D[O] = bfs(O)
        if not OS:
            return -1

        # O(MMO)
        DMM = {}
        for i in range(len(MS)):
            for j in range(i + 1, len(MS)):
                a, b = MS[i], MS[j]
                ans = inf
                for k in range(len(OS)):
                    c = OS[k]
                    ans = min(ans, D[a][c] + D[c][b])
                DMM[a, b] = ans
                DMM[b, a] = ans

        # O(MO)
        DSM = {}
        for i in range(len(MS)):
            ans = inf
            a = MS[i]
            for j in range(len(OS)):
                b = OS[j]
                ans = min(ans, D[S][b] + D[b][a])
            if ans == inf:
                return -1
            DSM[a] = ans

        MSZ = len(MS)
        MST = 1 << MSZ
        dp = [[inf] * MSZ for _ in range(MST)]
        for i in range(MSZ):
            st = 1 << i
            m = MS[i]
            dp[st][i] = DSM[m]

        # O(M*M*2^M)
        for st in range(MST):
            for i in range(MSZ):
                a = MS[i]
                if (st & (1 << i)) == 0:
                    continue
                for j in range(MSZ):
                    if (st & (1 << j)) != 0:
                        continue
                    b = MS[j]
                    st2 = st | (1 << j)
                    dp[st2][j] = min(dp[st2][j], dp[st][i] + DMM[a, b])

        ans = inf
        for i in range(MSZ):
            res = dp[MST - 1][i] + D[MS[i]][T]
            ans = min(ans, res)
        if ans == inf:
            ans = -1
        # O((M+O) * S) + O(MMO) + O(MM 2^M)
        return ans


cases = [
    (["S#O", "M.#", "M.T"], -1),
    (["S#O", "M.T", "M.."], 17),
    (["##TOO#O#", "OO##O.S#", "###.O###", "#..O#O##"], 5),
    (["......", "M....M", ".M#...", "....M.", "##.TM.", "...O..", ".S##O.", "M#..M.", "#....."], 60)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minimalSteps, cases)
