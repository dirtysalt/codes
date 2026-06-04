#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:

        def LIS(a):
            n = len(a)
            dp = []
            size = [0] * n

            for i in range(n):
                x = a[i]

                s, e = 0, len(dp) - 1
                while s <= e:
                    m = (s + e) // 2
                    if dp[m] >= x:
                        e = m - 1
                    else:
                        s = m + 1

                # insert at s
                size[i] = (s + 1)
                if s == len(dp):
                    dp.append(x)
                else:
                    dp[s] = min(dp[s], x)

            return size

        n = len(nums)
        a = LIS(nums)
        b = LIS(nums[::-1])
        ans = n
        for i in range(1, n - 1):
            x = a[i]
            y = b[n - 1 - i]
            remove = n - (x + y - 1)
            ans = min(ans, remove)

        return ans


cases = [
    ([1, 3, 1], 0),
    ([2, 1, 1, 5, 6, 2, 3, 1], 3),
    ([4, 3, 2, 1, 1, 2, 3, 1], 4),
    ([1, 2, 3, 4, 4, 3, 2, 1], 1),
    ([9, 8, 1, 7, 6, 5, 4, 3, 2, 1], 2)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minimumMountainRemovals, cases)
