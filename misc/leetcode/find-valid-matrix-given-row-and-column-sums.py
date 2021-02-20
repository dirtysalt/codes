#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n = len(rowSum)
        m = len(colSum)
        ans = [[0] * m for _ in range(n)]

        # 保证行之和始终满足，开始调整列
        for i in range(n):
            ans[i][0] = rowSum[i]

        for j in range(m):
            acc = 0
            for i in range(n):
                acc += ans[i][j]
                if acc > colSum[j]:
                    delta = acc - colSum[j]
                    ans[i][j + 1] += delta
                    ans[i][j] -= delta
                    acc -= delta

        # print(ans)
        return ans


import aatest_helper

cases = [
    ([3, 8], [4, 7], aatest_helper.ANYTHING),
    ([5, 7, 10], [8, 6, 8], aatest_helper.ANYTHING),
    ([14, 9], [6, 9, 8], aatest_helper.ANYTHING),
    ([1, 0], [1], aatest_helper.ANYTHING),
    ([0], [0], aatest_helper.ANYTHING),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().restoreMatrix, cases)
