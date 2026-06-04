#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        from collections import Counter
        cnt = Counter()
        n = len(nums)
        for i in range(4, n):
            for j in range(i + 2, n):
                c, d = nums[i], nums[j]
                g = gcd(c, d)
                cnt[c // g, d // g] += 1

        ans = 0
        for i in range(2, n - 2):
            for j in range(i - 1):
                a, b = nums[j], nums[i]
                g = gcd(a, b)
                ans += cnt[b // g, a // g]

            c = nums[i + 2]
            for j in range(i + 4, n):
                d = nums[j]
                g = gcd(c, d)
                cnt[c // g, d // g] -= 1

        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 2, 3, 4, 3, 6, 1], 1),
    ([3, 4, 3, 4, 3, 4, 3, 4], 3),
]

aatest_helper.run_test_cases(Solution().numberOfSubsequences, cases)

if __name__ == '__main__':
    pass
