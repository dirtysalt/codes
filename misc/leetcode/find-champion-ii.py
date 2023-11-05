#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        ind = [0] * n
        for u, v in edges:
            ind[v] += 1
        ans = []
        for i in range(n):
            if ind[i] == 0:
                ans.append(i)
        if len(ans) == 1: return ans[0]
        return -1


if __name__ == '__main__':
    pass
