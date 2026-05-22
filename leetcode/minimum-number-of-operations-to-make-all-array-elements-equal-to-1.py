#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        c = 0
        for i in range(n):
            if nums[i] == 1:
                c += 1
        if c > 0: return n - c

        def gcd(x, y):
            while y != 0:
                x, y = y, x % y
            return x

        ans = n
        for i in range(n):
            x = nums[i]
            j = i + 1
            while x != 1 and j < n:
                x = gcd(x, nums[j])
                j += 1
            if x == 1:
                ans = min(ans, j - i - 1)

        if ans == n: return -1
        return ans + (n - 1)


true, false, null = True, False, None
import aatest_helper

cases = [
    ([2, 6, 3, 4], 4),
    ([2, 10, 6, 14], -1),
    ([1, 2, 1], 1),
    ([1, 1, 1], 0)
]

aatest_helper.run_test_cases(Solution().minOperations, cases)

if __name__ == '__main__':
    pass
