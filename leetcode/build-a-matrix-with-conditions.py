#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def buildtop(conds):
            ind = [0] * (k + 1)
            adj = [[] for _ in range(k + 1)]
            for x, y in conds:
                ind[y] += 1
                adj[x].append(y)

            res = []
            from collections import deque
            dq = deque()
            for x in range(1, k + 1):
                if ind[x] == 0: dq.append(x)

            while dq:
                x = dq.popleft()
                res.append(x)
                for y in adj[x]:
                    ind[y] -= 1
                    if ind[y] == 0:
                        dq.append(y)
            if len(res) != k:
                return None
            return res

        row = buildtop(rowConditions)
        col = buildtop(colConditions)
        if not row or not col: return []
        R = {}
        C = {}
        for i in range(len(row)):
            x = row[i]
            R[x] = i
        for i in range(len(col)):
            x = col[i]
            C[x] = i
        ans = [[0] * k for _ in range(k)]
        for x in range(1, k + 1):
            r, c = R[x], C[x]
            ans[r][c] = x
        return ans


if __name__ == '__main__':
    pass
