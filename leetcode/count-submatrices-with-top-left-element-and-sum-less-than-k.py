#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        acc = [0] * (m + 1)

        ans = 0
        for i in range(n):
            tmp = [0] * (m + 1)
            for j in range(m):
                tmp[j + 1] = tmp[j] + grid[i][j]

            for j in range(m):
                acc[j + 1] += tmp[j + 1]
                if acc[j + 1] <= k:
                    ans += 1
            # print(acc)
        return ans


if __name__ == '__main__':
    pass
