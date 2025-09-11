#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        ind = [0] * n

        for a, b in roads:
            ind[a] += 1
            ind[b] += 1

        ind.sort()

        ans = 0
        for i in range(n):
            ans += ind[i] * (i + 1)
        return ans


if __name__ == '__main__':
    pass
