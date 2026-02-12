#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import bisect
from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)

        p = 0
        for i in range(1, n):
            if arr[i - 1] <= arr[i]:
                p = i
            else:
                break
        left = arr[:p + 1]

        p = n - 1
        for i in reversed(range(n - 1)):
            if arr[i] <= arr[i + 1]:
                p = i
            else:
                break
        right = arr[p:]

        ans = n - max(len(left), len(right))
        if ans == 0: return ans
        for i in range(len(left)):
            x = left[i]
            idx = bisect.bisect_left(right, x)
            size = (i + 1) + (len(right) - idx)
            ans = min(ans, n - size)
        return ans


true, false, null = True, False, None
cases = [
    ([1, 2, 3, 10, 4, 2, 3, 5], 3),
    ([5, 4, 3, 2, 1], 4),
    ([1], 0),
    ([1, 2, 3], 0),
    ([1, 2, 3, 10, 0, 7, 8, 9], 2),
    ([6, 3, 10, 11, 15, 20, 13, 3, 18, 12], 8)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().findLengthOfShortestSubarray, cases)

if __name__ == '__main__':
    pass
