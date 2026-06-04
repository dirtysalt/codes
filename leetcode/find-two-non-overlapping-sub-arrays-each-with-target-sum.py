#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        inf = 1 << 30

        def test(arr):
            n = len(arr)
            res = [inf] * n

            j = 0
            acc = 0
            sz = inf
            for i in range(n):
                acc += arr[i]
                while j <= i and acc > target:
                    acc -= arr[j]
                    j += 1

                if acc == target and (i - j + 1) != 0:
                    sz = min(sz, i - j + 1)
                res[i] = sz

            return res

        left = test(arr)
        right = test(arr[::-1])
        n = len(arr)
        ans = inf
        for i in range(n - 1):
            j = n - i - 2
            if left[i] != inf and right[j] != inf:
                ans = min(ans, left[i] + right[j])
        if ans == inf:
            ans = -1
        return ans


cases = [
    ([3, 2, 2, 4, 3], 3, 2),
    ([7, 3, 4, 7], 7, 2),
    ([4, 3, 2, 6, 2, 3, 4], 6, -1),
    ([3, 1, 1, 1, 5, 1, 2, 1], 3, 3),
    ([1, 2, 2, 3, 2, 6, 7, 2, 1, 4, 8], 5, 4),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minSumOfLengths, cases)
