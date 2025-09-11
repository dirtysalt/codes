#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        left = nums.copy()
        for i in range(1, n):
            left[i] = min(left[i - 1], nums[i])

        st = []
        for i in reversed(range(n)):
            if nums[i] > left[i]:
                # find possible k
                while st and st[-1] <= left[i]:
                    st.pop()
                if st and st[-1] < nums[i]:
                    return True
                st.append(nums[i])
        return False


cases = [
    ([3, 1, 4, 2], True),
    ([1, 2, 3, 4, ], False),
    ([-1, 3, 2, 0], True)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().find132pattern, cases)
