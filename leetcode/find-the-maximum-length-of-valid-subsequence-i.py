#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        k = 2
        pos = [[-1] * k for _ in range(n + 1)]
        last = [-1] * k
        for i in reversed(range(n)):
            last[nums[i] % k] = i
            pos[i] = last.copy()

        # print(pos)
        import functools
        @functools.cache
        def check(i, rem):
            j = pos[i + 1][rem - (nums[i] % k)]
            if j == -1: return 0
            return check(j, rem) + 1

        ans = 0
        for i in range(n - 1):
            for rem in range(k):
                a = check(i, rem)
                ans = max(ans, a)
        return ans + 1


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 2, 3, 4], 4),
    ([1, 2, 1, 1, 2, 1, 2], 6),
    ([1, 3], 2)
]

aatest_helper.run_test_cases(Solution().maximumLength, cases)

if __name__ == '__main__':
    pass
