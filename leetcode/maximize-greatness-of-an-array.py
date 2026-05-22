#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        from sortedcontainers import SortedList
        sl = SortedList(nums)

        ans = 0
        for x in nums:
            idx = sl.bisect_left(x + 1)
            if 0 <= idx < len(sl):
                # print(sl[idx])
                ans += 1
                sl.remove(sl[idx])
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 3, 5, 2, 1, 3, 1], 4),
    ([1, 2, 3, 4], 3),
]

aatest_helper.run_test_cases(Solution().maximizeGreatness, cases)

if __name__ == '__main__':
    pass
