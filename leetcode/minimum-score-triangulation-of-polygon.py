#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List

from aatest_helper import run_test_cases


class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        cache = {}
        n = len(A)

        def compute(i, j, k):

            key = '{}.{}.{}'.format(i, j, k)
            if key in cache:
                return cache[key]

            value = 1 << 30
            for idx in range(j + 1, k + 1):
                # tri(i, j, idx) + compute(i, idx, k) + compute(j, j+1, idx)
                res = A[i] * A[j] * A[idx]
                if res >= value:
                    continue

                if idx < k:
                    res += compute(i, idx, k)
                if (j + 1) < idx:
                    res += compute(j, j + 1, idx)
                value = min(res, value)

            cache[key] = value
            return value

        res = compute(0, 1, n - 1)
        return res


def test():
    cases = [
        ([1, 2, 3], 6),
        ([3, 7, 4, 5], 144),
        ([1, 3, 1, 4, 1, 5], 13)
    ]
    sol = Solution()
    fn = sol.minScoreTriangulation
    run_test_cases(fn, cases)


if __name__ == '__main__':
    test()
