#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        n = len(A)

        def test(L, M):
            a = sum(A[:L])
            ma = a

            b = sum(A[L:L + M])
            ans = a + b
            # print(L + M - 1, a, b)
            for i in range(L + M, n):
                b += A[i] - A[i - M]
                a = a + A[i - M] - A[i - M - L]
                ma = max(ma, a)
                # print('#{}, a = {}, ma = {}, b = {}'.format(i, a, ma, b))
                ans = max(ans, ma + b)
            return ans

        ans = test(L, M)
        if L != M:
            ans = max(ans, test(M, L))
        return ans


cases = [
    ([0, 6, 5, 2, 2, 5, 1, 9, 4], 1, 2, 20),
    ([3, 8, 1, 3, 2, 1, 8, 9, 0], 3, 2, 29),
    ([2, 1, 5, 6, 0, 9, 5, 0, 3, 8], 4, 3, 31),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxSumTwoNoOverlap, cases)
