#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n, m = len(matrix), len(matrix[0])
        from collections import Counter

        if n > m:
            matrix = list(zip(*matrix))
            n, m = m, n

        # O(n^2 * m)
        self.ans = 0
        for i in range(n):
            # print('===== {} ===='.format(i))
            dp = [0] * m
            for j in range(i, n):
                tmp = 0
                c = Counter()
                c[tmp] = 1
                for k in range(m):
                    tmp += matrix[j][k]
                    dp[k] += tmp

                    lookup = dp[k] - target
                    self.ans += c[lookup]
                    c[dp[k]] += 1
                # print(dp)
        return self.ans


cases = [
    ([[0, 1, 0], [1, 1, 1], [0, 1, 0]], 0, 4),
    ([[1, -1], [-1, 1]], 0, 5)
]
import aatest_helper

aatest_helper.run_test_cases(Solution().numSubmatrixSumTarget, cases)
