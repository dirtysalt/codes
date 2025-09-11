#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ans = 0

        if True:
            # center lines.
            cnt = [0] * 4
            if n % 2 == 1:
                for j in range(m // 2):
                    x, y = grid[n // 2][j], grid[n // 2][m - 1 - j]
                    cnt[2 * x + y] += 1
            if m % 2 == 1:
                for i in range(n // 2):
                    x, y = grid[i][m // 2], grid[n - 1 - i][m // 2]
                    cnt[2 * x + y] += 1

            # c (0,1)(1,0)
            # b (1,1)
            c, b = cnt[1] + cnt[2], cnt[3]
            if b % 2 == 1:
                if c > 0:
                    # 1,0 -> 1,1
                    ans += 1
                    c -= 1
                else:
                    # 1,1 -> 0, 0
                    ans += 2
            ans += c

            # center point.
            if n % 2 and m % 2 and grid[n // 2][m // 2]:
                ans += 1

        # print(ans)
        for i in range(n // 2):
            for j in range(m // 2):
                p = [(i, j), (n - 1 - i, j), (i, m - 1 - j), (n - 1 - i, m - 1 - j)]
                # print(p)
                a, b = 0, 0
                for x, y in p:
                    if grid[x][y] == 1:
                        b += 1
                    else:
                        a += 1
                ans += min(a, b)
        return ans


if __name__ == '__main__':
    pass
