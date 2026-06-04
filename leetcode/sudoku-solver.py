#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [0] * 9
        col = [0] * 9
        sqr = [0] * 9
        ps = []
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c == '.':
                    ps.append((i, j))
                    continue
                v = int(c)
                v1 = (1 << v)
                row[i] = row[i] | v1
                col[j] = col[j] | v1
                s = (i // 3) * 3 + (j // 3)
                sqr[s] = sqr[s] | v1

        place = []

        def dfs(k):
            if k == len(ps):
                return True
            i, j = ps[k]
            for v in range(1, 1 + 9):
                v1 = (1 << v)
                if row[i] & v1: continue
                if col[j] & v1: continue
                s = (i // 3) * 3 + (j // 3)
                if sqr[s] & v1: continue

                row[i] |= v1
                col[j] |= v1
                sqr[s] |= v1
                place.append(v)
                if dfs(k + 1):
                    return True
                place.pop()
                v2 = ~v1
                row[i] &= v2
                col[j] &= v2
                sqr[s] &= v2

        dfs(0)
        # print(ps, place)
        k = 0
        for i in range(9):
            s = board[i]
            for j in range(9):
                if s[j] == '.':
                    s[j] = str(place[k])
                    k += 1
            board[i] = s
