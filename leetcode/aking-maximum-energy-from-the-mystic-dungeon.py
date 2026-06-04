#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:

        n = len(energy)
        import functools
        @functools.cache
        def dfs(i):
            j = i + k
            if 0 <= j < n:
                return dfs(j) + energy[i]
            return energy[i]

        ans = dfs(0)
        for i in range(n):
            c = dfs(i)
            ans = max(ans, c)
        return ans


if __name__ == '__main__':
    pass
