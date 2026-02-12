#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minMaxSubarraySum(self, nums: List[int], k: int) -> int:
        def compute(a, b, k):
            ans = 0
            for i in range(0, min(k, a + 1)):
                j = min(k - 1 - i, b)
                ans += (j + 1)
            return ans

        def compute(a, b, k):
            m = min(k, a + 1)
            if m == 0:
                return 0
            if (k - 1) <= b:
                return m * k - m * (m - 1) // 2
            else:
                i0 = (k - 1) - b
                split = min(i0 + 1, m)
                sum_part1 = split * (b + 1)
                remaining = m - split
                if remaining <= 0:
                    return sum_part1
                else:
                    sum_part2 = remaining * k - (split * remaining + remaining * (remaining - 1) // 2)
                    return sum_part1 + sum_part2

        def build(nums, fn):
            n = len(nums)
            left = [-1] * n
            for i in range(1, n):
                j = i - 1
                while j >= 0 and fn(nums[i], nums[j]) < 0:
                    j = left[j]
                left[i] = j

            right = [n] * n
            for i in reversed(range(n - 1)):
                j = i + 1
                while j < n and fn(nums[i], nums[j]) <= 0:
                    j = right[j]
                right[i] = j

            ans = 0
            for i in range(n):
                a = (i - 1 - left[i])
                b = (right[i] - 1 - i)
                ans += nums[i] * compute(a, b, k)
            return ans

        def minf(x, y):
            if x == y: return 0
            return x - y

        def maxf(x, y):
            if x == y: return 0
            return y - x

        A = build(nums, minf)
        B = build(nums, maxf)
        return A + B


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 2, 3], 2, 20),
    ([1, -3, 1], 2, -6),
]

aatest_helper.run_test_cases(Solution().minMaxSubarraySum, cases)

if __name__ == '__main__':
    pass
