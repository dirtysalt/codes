#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        ans, c = 0, 0
        for x in reversed(nums):
            if c < x:
                ans = max(ans, c)
                c = 0
            c += x
        ans = max(ans, c)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([2, 3, 7, 9, 3], 21),
    ([5, 3, 3], 11),
]

aatest_helper.run_test_cases(Solution().maxArrayValue, cases)

if __name__ == '__main__':
    pass
