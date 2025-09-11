#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    """
    @param matrix: List[List[int]]
    @param k: a integer
    @return: return a integer
    """

    def kthSmallest(self, matrix, k):
        # write your code here

        n = len(matrix)

        def rank(r, c):
            low, high = c + 1, c + 1
            import bisect
            for r2 in reversed(range(0, r)):
                if matrix[r][c] >= matrix[r2][-1]:
                    low += (r2 + 1) * n
                    high += (r2 + 1) * n
                    break

                x = bisect.bisect_left(matrix[r2], matrix[r][c])
                y = bisect.bisect_right(matrix[r2], matrix[r][c])
                low += x
                high += y

            for r2 in range(r + 1, n):
                if matrix[r][c] < matrix[r2][0]:
                    break
                x = bisect.bisect_left(matrix[r2], matrix[r][c])
                y = bisect.bisect_right(matrix[r2], matrix[r][c])
                low += x
                high += y
            return low, high

        r, c = 0, n - 1
        while True:
            low, high = rank(r, c)
            if low <= k <= high:
                return matrix[r][c]
            if k < low:
                c -= 1
            else:
                r += 1
        raise RuntimeError("false path")


cases = [
    ([
         [1, 5, 9],
         [10, 11, 13],
         [12, 13, 15]
     ], 7, 13),

    ([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5, 5)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().kthSmallest, cases)
