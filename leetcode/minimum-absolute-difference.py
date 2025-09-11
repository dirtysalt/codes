#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = []

        n = len(arr)
        _min = 10 ** 9
        for i in range(1, n):
            diff = arr[i] - arr[i - 1]
            if diff <= _min:
                if diff < _min:
                    ans.clear()
                    _min = diff
                ans.append([arr[i - 1], arr[i]])

        return ans


cases = [
    ([3, 8, -10, 23, 19, -4, -14, 27], [[-14, -10], [19, 23], [23, 27]])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minimumAbsDifference, cases)
