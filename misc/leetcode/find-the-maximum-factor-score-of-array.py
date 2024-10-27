#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        def process(seq):
            if not seq: return 0
            g, l = seq[0], seq[0]
            for x in seq:
                g = gcd(g, x)
                l = x * l // gcd(x, l)
            # print(seq, g, l)
            return g * l

        ans = process(nums)
        for i in range(len(nums)):
            r = process(nums[:i] + nums[i + 1:])
            ans = max(ans, r)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([2, 4, 8, 16], 64),
    ([1, 2, 3, 4, 5], 60),
]

aatest_helper.run_test_cases(Solution().maxScore, cases)

if __name__ == '__main__':
    pass
