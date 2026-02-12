#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        def split(arr):
            return [x for x in arr if x % 2 == 0], [x for x in arr if x % 2 == 1]

        def check(a, b):
            assert (len(a) == len(b))
            delta = 0
            for i in range(len(a)):
                delta += abs(a[i] - b[i])
            return delta

        nums.sort()
        target.sort()
        a, b = split(nums)
        c, d = split(target)
        r0 = check(a, c)
        r1 = check(b, d)
        r = r0 + r1
        assert (r % 4 == 0)
        return r // 4


true, false, null = True, False, None
cases = [
    ([8, 12, 6], [2, 14, 10], 2),
    ([1, 2, 5], [4, 1, 3], 1),
    ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1], 0),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().makeSimilar, cases)

if __name__ == '__main__':
    pass
