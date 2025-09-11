#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        from sortedcontainers import SortedList
        sl = SortedList()
        sl.add(nums[0])
        diff = nums[0] - nums[1]

        n = len(nums)
        ans = 0
        for k in range(2, n):
            diff = max(diff, sl[-1] - nums[k - 1])
            r = diff * nums[k]
            ans = max(ans, r)
            sl.add(nums[k - 1])
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([12, 6, 1, 2, 7], 77),
    ([1, 10, 3, 4, 19], 133),
    ([1, 2, 3], 0),
]

aatest_helper.run_test_cases(Solution().maximumTripletValue, cases)

if __name__ == '__main__':
    pass
