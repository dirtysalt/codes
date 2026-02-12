#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:

        from sortedcontainers import SortedList
        sl = SortedList()
        n = len(nums)
        for i in range(x, n):
            sl.add(nums[i])

        ans = 10 ** 9
        for i in range(n - x):
            idx = sl.bisect_left(nums[i])
            if 0 <= idx < len(sl):
                d = abs(sl[idx] - nums[i])
                ans = min(ans, d)
            if 0 <= (idx - 1) < len(sl):
                d = abs(sl[idx - 1] - nums[i])
                ans = min(ans, d)
            sl.remove(nums[i + x])
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([4, 3, 2, 4], 2, 0),
    ([5, 3, 2, 10, 15], 1, 1),
    ([1, 2, 3, 4], 3, 3,),
    ([330702844, 313481959, 239224564, 609763700, 170531905], 0, 0)
]

aatest_helper.run_test_cases(Solution().minAbsoluteDifference, cases)

if __name__ == '__main__':
    pass
