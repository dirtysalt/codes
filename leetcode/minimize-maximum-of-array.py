#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def check(x):
            n = len(nums)
            delta = 0
            for i in range(n):
                if nums[i] > x:
                    req = nums[i] - x
                    if delta >= req:
                        delta -= req
                    else:
                        return False
                else:
                    delta += (x - nums[i])
            return True

        s, e = 0, max(nums)
        while s <= e:
            m = (s + e) // 2
            if check(m):
                e = m - 1
            else:
                s = m + 1
        return s


true, false, null = True, False, None
cases = [
    ([3, 7, 1, 6], 5),
    ([10, 1], 10),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minimizeArrayValue, cases)

if __name__ == '__main__':
    pass
