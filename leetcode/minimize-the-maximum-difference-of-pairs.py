#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        n = len(nums)
        nums.sort()

        def test(val):
            idx = 0
            c = 0
            while (idx + 1) < n:
                if (nums[idx + 1] - nums[idx]) <= val:
                    idx += 2
                    c += 1
                else:
                    idx += 1
            return c >= p

        s, e = 0, nums[-1] - nums[0]
        while s <= e:
            m = (s + e) // 2
            if test(m):
                e = m - 1
            else:
                s = m + 1
        return s


true, false, null = True, False, None
import aatest_helper

cases = [
    ([10, 1, 2, 7, 1, 3], 2, 1),
    ([4, 2, 1, 2], 1, 0),
    ([3, 4, 2, 3, 2, 1, 2], 3, 1),
]

aatest_helper.run_test_cases(Solution().minimizeMax, cases)

if __name__ == '__main__':
    pass
