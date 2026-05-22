#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import functools
from typing import List


class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        nums.sort()
        MOD = 10 ** 9 + 7

        def search(cost, i, j):

            @functools.cache
            def left_search(idx, exp):
                if exp == 0: return 1
                r = 0
                for ii in reversed(range(0, idx)):
                    if nums[idx] - nums[ii] <= cost: continue
                    r += left_search(ii, exp - 1)
                return r

            @functools.cache
            def right_search(idx, exp):
                if exp == 0: return 1
                r = 0
                for ii in range(idx + 1, len(nums)):
                    if nums[ii] - nums[idx] < cost: continue
                    r += right_search(ii, exp - 1)
                return r

            r = 0
            for kk in range(0, k - 2 + 1):
                r0 = left_search(i, kk)
                r1 = right_search(j, k - 2 - kk)
                r += r0 * r1
            return r

        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                cost = nums[j] - nums[i]
                number = search(cost, i, j)
                # print(nums[i:j + 1], cost, number)
                ans += cost * number
        return ans % MOD


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 2, 3, 4, ], 3, 4),
    ([2, 2], 2, 0),
    ([4, 3, -1, ], 2, 10),
    ([3, 2, -8, 6], 4, 1),
]

aatest_helper.run_test_cases(Solution().sumOfPowers, cases)

if __name__ == '__main__':
    pass
