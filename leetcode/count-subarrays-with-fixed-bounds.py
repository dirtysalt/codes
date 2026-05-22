#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)

        j, a, b = -1, -1, -1
        ans = 0
        for i in range(n):
            x = nums[i]
            if minK <= x <= maxK:
                if j == -1:
                    j = i
                if x == minK:
                    a = max(a, i)
                if x == maxK:
                    b = max(b, i)

                if a != -1 and b != -1:
                    p = min(a, b)
                    ans += p - j + 1
            else:
                j, a, b = -1, -1, -1

        return ans


true, false, null = True, False, None
cases = [
    ([1, 3, 5, 2, 7, 5], 1, 5, 2),
    ([1, 1, 1, 1], 1, 1, 10),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().countSubarrays, cases)

if __name__ == '__main__':
    pass
