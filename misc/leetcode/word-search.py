#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        if n == 0: return False
        m = len(board[0])
        if m == 0: return False

        visited = [[0] * m for _ in range(n)]

        def dfs(i, j, idx):
            if board[i][j] != word[idx]:
                return False
            if idx == len(word) - 1:
                return True
            visited[i][j] = 1
            ok = False
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni = i + di
                nj = j + dj
                if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
                    ok = ok or dfs(ni, nj, idx + 1)
                    if ok:
                        break
            visited[i][j] = 0
            return ok

        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0):
                    return True
        return False


cases = [
    ([
         ['A', 'B', 'C', 'E'],
         ['S', 'F', 'C', 'S'],
         ['A', 'D', 'E', 'E']
     ], 'ABCCED', True),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().exist, cases)
