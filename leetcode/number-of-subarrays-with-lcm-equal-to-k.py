#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        def lcm(a, b):
            g = gcd(a, b)
            return (a * b) // g

        ans = 0
        for i in range(n):
            a = nums[i]
            for j in range(i, n):
                a = lcm(a, nums[j])
                if a == k:
                    ans += 1
                if a > k:
                    break
        return ans


true, false, null = True, False, None
cases = [
    ([3, 6, 2, 7, 1], 6, 4),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().subarrayLCM, cases)

if __name__ == '__main__':
    pass
