#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)

        def possible_values(tmp):
            values = set([0])
            for x in tmp:
                update = []
                for y in values:
                    update.append(x + y)
                values.update(update)
            return values

        A = possible_values(nums[:n // 2])
        B = possible_values(nums[n // 2:])
        A = list(A)
        A.sort()

        # print(A, B)
        ans = 1 << 31
        for x in B:
            exp = goal - x
            s, e = 0, len(A) - 1
            while s <= e:
                m = (s + e) // 2
                if A[m] >= exp:
                    e = m - 1
                else:
                    s = m + 1
            ps = [s - 1, s, s + 1]
            for p in ps:
                if 0 <= p < len(A):
                    ans = min(abs(A[p] + x - goal), ans)
        return ans


cases = [
    ([5, -7, 3, 5], 6, 0),
    ([7, -9, 15, -2], -5, 1),
    ([1, 2, 3], -7, 7)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minAbsDifference, cases)
