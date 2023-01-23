#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        n, m = len(board), len(board[0])
        ans = 0

        for i in range(n):
            for j in range(m):
                if board[i][j] == '.':
                    continue
                if (i > 0 and board[i - 1][j] == 'X') or (j > 0 and board[i][j - 1] == 'X'):
                    continue
                ans += 1
        return ans
