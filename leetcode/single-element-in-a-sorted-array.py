#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        import functools
        ans = functools.reduce(lambda x, y: x ^ y, nums, 0)
        return ans


class Solution2:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        s, e = 0, n - 1
        while s < e:
            m = (s + e) // 2
            if (m - 1) >= 0 and nums[m] == nums[m - 1]:
                sz = m - 2 - s + 1
                if sz % 2 == 1:
                    e = m - 2
                else:
                    s = m + 1

            elif (m + 1) < n and nums[m] == nums[m + 1]:
                sz = e - (m + 2) + 1
                if sz % 2 == 1:
                    s = m + 2
                else:
                    e = m - 1

            else:
                return nums[m]

        assert s == e
        return nums[s]


cases = [
    ([1, 1, 2, 3, 3, 4, 4, 8, 8], 2),
    ([3, 3, 7, 7, 10, 11, 11], 10,),
    ([1, 1, 2, 3, 3, ], 2)
]

import aatest_helper

aatest_helper.run_test_cases(Solution2().singleNonDuplicate, cases)
