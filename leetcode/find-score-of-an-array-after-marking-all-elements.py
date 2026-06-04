#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        from sortedcontainers import SortedList
        sl = SortedList((v, i) for (i, v) in enumerate(nums))
        ans = 0

        def rem(i):
            if 0 <= i < len(nums):
                v = nums[i]
                if (v, i) in sl:
                    sl.remove((v, i))

        while sl:
            (v, i) = sl[0]
            ans += v
            rem(i + 1)
            rem(i - 1)
            rem(i)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([2, 1, 3, 4, 5, 2], 7),
    ([2, 3, 5, 1, 3, 2], 5),
]

aatest_helper.run_test_cases(Solution().findScore, cases)

if __name__ == '__main__':
    pass
