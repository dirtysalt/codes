#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        n, m = len(mat), len(mat[0])

        def get_sum(tp):
            res = 0
            for i in range(n):
                res += mat[i][tp[i]]
            return res

        def next_tps(tp):
            res = []
            for i in range(n):
                tp2 = list(tp)
                tp2[i] += 1
                if tp2[i] < m:
                    res.append(tuple(tp2))
            return res

        import heapq
        hp = []
        visited = set()
        start = tuple([0] * n)
        hp.append((get_sum(start), start))
        visited.add(start)
        ans = None

        while hp:
            (x, tp) = hp[0]
            heapq.heappop(hp)
            print(x, tp)
            k -= 1
            if k == 0:
                ans = x
                break
            tps = next_tps(tp)
            for tp in tps:
                if tp not in visited:
                    visited.add(tp)
                    heapq.heappush(hp, (get_sum(tp), tp))
        return ans
