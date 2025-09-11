#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        st = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] >= st[-1]:
                st.append(nums[i])
        return len(st)


true, false, null = True, False, None
import aatest_helper

cases = [
    ([4, 2, 5, 3, 5], 3),
    ([1, 2, 3], 3),
]

aatest_helper.run_test_cases(Solution().maximumPossibleSize, cases)

if __name__ == '__main__':
    pass
