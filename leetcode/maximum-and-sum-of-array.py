#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import functools
from typing import List

class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        # remove unused numbers.
        tmp = []
        for x in nums:
            if all((x & (i + 1)) == 0 for i in range(numSlots)):
                continue
            tmp.append(x)
        nums = tmp

        # choose effective slots.
        st = [0] * numSlots
        pref = [] * len(nums)
        for i in range(len(nums)):
            slots = []
            for j in range(numSlots):
                if nums[i] & (j + 1) != 0:
                    slots.append(j)
            slots.sort(key=lambda x: (x + 1) & (nums[i]), reverse=True)
            pref.append(slots)

        @functools.lru_cache(maxsize=None)
        def dfs(i, st):
            if i == len(nums):
                return 0

            res = 0
            for j in pref[i]:
                b = (st >> (2 * j)) & 0x3
                if b < 2:
                    v = nums[i] & (j + 1)
                    res = max(res, v + dfs(i + 1, st | ((b + 1) << (2 * j))))

            return res

        ans = dfs(0, 0)
        return ans

true, false, null = True, False, None
cases = [
    ([1, 2, 3, 4, 5, 6], 3, 9),
    ([1, 3, 10, 4, 7, 1], 9, 24),
    ([14, 7, 9, 8, 2, 4, 11, 1, 9], 8, 40),
    ([8, 13, 3, 15, 3, 15, 2, 15, 5, 7, 6], 8, 60),
    ([15, 13, 4, 4, 11, 6, 6, 12, 15, 7, 3, 12, 13, 7], 8, 70),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maximumANDSum, cases)

if __name__ == '__main__':
    pass
