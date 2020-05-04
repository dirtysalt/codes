#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []

        def make_place(place):
            assert len(place) == n
            res = []
            for i in range(n):
                j = place[i]
                t = ['.'] * n
                t[j] = 'Q'
                res.append(''.join(t))
            # print(place, res)
            return res

        def dfs(i, place):
            if i == n:
                ans.append(make_place(place))
                return

            for j in range(n):
                ok = True
                for r in range(len(place)):
                    c = place[r]
                    if (i - r) == (j - c) or (i - r) == (c - j) or c == j:
                        ok = False
                        break
                if ok:
                    place.append(j)
                    dfs(i + 1, place)
                    place.pop()

        dfs(0, [])
        return ans
