#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()

        def test(k):
            a = nums[:k]
            b = nums[-k:]
            for x, y in zip(a, b):
                if 2 * x > y:
                    return False
            return True

        s, e = 1, len(nums) // 2
        while s <= e:
            m = (s + e) // 2
            if test(m):
                s = m + 1
            else:
                e = m - 1
        return 2 * e


true, false, null = True, False, None
import aatest_helper

cases = [
    ([3, 5, 2, 4], 2),
    ([9, 2, 5, 4], 4),
    ([7, 6, 8], 0),
]

aatest_helper.run_test_cases(Solution().maxNumOfMarkedIndices, cases)

if __name__ == '__main__':
    pass
