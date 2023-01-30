#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1: return 0
        n = len(weights)

        arr = []
        for i in range(1, n):
            arr.append(weights[i - 1] + weights[i])
        arr.sort()

        A = sum(arr[-(k - 1):])
        B = sum(arr[:(k - 1)])
        ans = A - B
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 3, 5, 1], 2, 4),
    ([1, 3], 2, 0),
    ([1, 4, 2, 5, 2], 3, 3),
    ([25, 74, 16, 51, 12, 48, 15, 5], 1, 0)
]

aatest_helper.run_test_cases(Solution().putMarbles, cases)

if __name__ == '__main__':
    pass
