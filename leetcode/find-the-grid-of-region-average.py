#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        n, m = len(image), len(image[0])
        avg = {}

        def check_region(i, j):
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    x, y = i + dx, j + dy
                    # for a, b in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                    for a, b in ((0, 1), (1, 0)):
                        x2, y2 = x + a, y + b
                        if i - 1 <= x2 <= i + 1 and j - 1 <= y2 <= j + 1:
                            if abs(image[x2][y2] - image[x][y]) > threshold:
                                return False
            return True

        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if check_region(i, j):
                    t = 0
                    for dx in (-1, 0, 1):
                        for dy in (-1, 0, 1):
                            t += image[i + dx][j + dy]
                    avg[(i, j)] = t // 9

        ans = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                a, b = 0, 0
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        if (i + dx, j + dy) in avg:
                            a += avg[(i + dx, j + dy)]
                            b += 1
                ans[i][j] = a // b if b else image[i][j]
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(image=[[5, 6, 7, 10], [8, 9, 10, 10], [11, 12, 13, 10]], threshold=3
                              , res=[[9, 9, 9, 9], [9, 9, 9, 9], [9, 9, 9, 9]]),
    aatest_helper.OrderedDict(image=[[10, 20, 30], [15, 25, 35], [20, 30, 40], [25, 35, 45]], threshold=12,
                              res=[[25, 25, 25], [27, 27, 27], [27, 27, 27], [30, 30, 30]]),
    aatest_helper.OrderedDict(image=[[5, 6, 7], [8, 9, 10], [11, 12, 13]], threshold=1,
                              res=[[5, 6, 7], [8, 9, 10], [11, 12, 13]]),
]

aatest_helper.run_test_cases(Solution().resultGrid, cases)

if __name__ == '__main__':
    pass
