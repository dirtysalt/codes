#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        if len(A) == 1:
            return 0

        n = len(A)

        def test(a, b):
            if a > b:
                a, b = b, a

            for i in range(2, n):
                opts = []
                x = A[i]
                if (x + K) >= b:
                    opts.append((x + K - a, a, x + K))
                elif (x + K) <= a:
                    opts.append((b - (x + K), x + K, b))
                else:
                    opts.append((b - a, a, b))

                if (x - K) >= b:
                    opts.append((x - K - a, a, x - K))
                elif (x - K) <= a:
                    opts.append((b - x + K, x - K, b))
                else:
                    opts.append((b - a, a, b))

                opts.sort()
                a, b = opts[0][1:]

            ans = b - a
            return ans

        res = []
        res.append(test(A[0] - K, A[1] - K))
        res.append(test(A[0] - K, A[1] + K))
        res.append(test(A[0] + K, A[1] - K))
        res.append(test(A[0] + K, A[1] + K))

        ans = min(res)
        return ans


cases = [
    # ([0, 10, ], 2, 6),
    # ([1, 3, 6], 3, 3),
    # ([7, 8, 8], 5, 1),
    ([10, 3, 1, 2, 4, 6], 2, 5)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().smallestRangeII, cases)
