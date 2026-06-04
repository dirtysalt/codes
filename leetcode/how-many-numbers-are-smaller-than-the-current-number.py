#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [(nums[i], i) for i in range(n)]
        res.sort()
        ans = [-1] * n

        i = 0
        while i < n:
            j = i
            while j < n and res[j][0] == res[i][0]:
                p = res[j][1]
                ans[p] = i
                j += 1
            i = j
        return ans


cases = [
    ([8, 1, 2, 2, 3], [4, 0, 1, 1, 3]),
    ([6, 5, 4, 8], [2, 1, 0, 3])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().smallerNumbersThanCurrent, cases)
