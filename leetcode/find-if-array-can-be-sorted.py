#!/usr/bin/env python
# w'd coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        data = []
        j = 0

        def ones(x):
            c = 0
            while x:
                c += x & 0x1
                x = x >> 1
            return c

        for i in range(len(nums)):
            if ones(nums[i]) != ones(nums[j]):
                data.extend(sorted(nums[j:i]))
                j = i
        data.extend(sorted(nums[j:]))

        return data == sorted(data)


true, false, null = True, False, None
import aatest_helper

cases = [
    ([8, 4, 2, 30, 15], true),
    ([1, 2, 3, 4, 5], true),
    ([3, 16, 8, 4, 2], false),
]

aatest_helper.run_test_cases(Solution().canSortArray, cases)

if __name__ == '__main__':
    pass
