#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        def pow(x, mod):
            ans = 1
            base = 2
            while x:
                if x % 2 == 1:
                    ans = (ans * base) % mod
                base = (base * base) % mod
                x = x >> 1
            return ans

        MOD = 10 ** 9 + 7

        nums.sort()
        i, j = 0, len(nums) - 1
        ans = 0
        while i < j:
            if nums[i] + nums[j] > target:
                j -= 1
                continue
            d = pow(j-i ,MOD)
            ans = (ans + d - 1 + MOD) % MOD
            i += 1

        for x in nums:
            if 2 * x <= target:
                ans = (ans + 1) % MOD
            else:
                break

        return ans


import aatest_helper

cases = [
    ([3,5,6,7], 9, 4),
    ([5,2,4,1,7,6,8], 16,127),
    ([3,3,6,8], 10, 6),
    ([2,3,3,4,6,7], 12, 61)
]

aatest_helper.run_test_cases(Solution().numSubseq, cases)
