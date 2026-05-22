#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List

class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            if k % 2 == 1:
                return -1
            return nums[0]

        if k in (0, 1):
            return nums[k]

        ans = max(nums[:k - 1])
        if len(nums) > k:
            ans = max(ans, nums[k])
        return ans

true, false, null = True, False, None
cases = [
    ([35, 43, 23, 86, 23, 45, 84, 2, 18, 83, 79, 28, 54, 81, 12, 94, 14, 0, 0, 29, 94, 12, 13, 1, 48, 85, 22, 95, 24, 5,
      73, 10, 96, 97, 72, 41, 52, 1, 91, 3, 20, 22, 41, 98, 70, 20, 52, 48, 91, 84, 16, 30, 27, 35, 69, 33, 67, 18, 4,
      53, 86, 78, 26, 83, 13, 96, 29, 15, 34, 80, 16, 49], 15, 94),
    ([4, 6, 1, 0, 6, 2, 4], 0, 4),
    ([5, 2, 2, 4, 0, 6], 4, 5),
    ([2], 1, -1),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maximumTop, cases)

if __name__ == '__main__':
    pass
