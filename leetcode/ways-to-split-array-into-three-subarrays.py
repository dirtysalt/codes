#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [0] * (n + 1)
        for i in range(n):
            arr[i] = arr[i - 1] + nums[i]

        ans = 0
        for l in range(n):
            # [0 .. l]
            a = arr[l]
            b = arr[n - 1] - arr[l]
            # [l+1 .. m]
            # [m+1 .. n-1]
            c = arr[l] + a
            d = b // 2 + a

            import bisect
            i = bisect.bisect_left(arr, c, l + 1, n - 1)
            j = bisect.bisect_right(arr, d, i, n - 1)
            space = j - i
            if space > 0:
                # print(i, j, b)
                ans += space

        MOD = 10 ** 9 + 7
        ans = ans % MOD
        return ans


cases = [
    ([1, 1, 1], 1),
    ([1, 2, 2, 2, 5, 0], 3),
    ([3, 2, 1], 0),
    ([0, 3, 3], 1),
    ([0, 0, 0, 0], 3),
    # ([0] * 100000, 999849973)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().waysToSplit, cases)
