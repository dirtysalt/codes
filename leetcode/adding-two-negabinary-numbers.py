#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        n = max(len(arr1), len(arr2))
        tmp = [0] * n
        for i in reversed(range(len(arr1))):
            tmp[i] += arr1[len(arr1) - 1 - i]
        for i in reversed(range(len(arr2))):
            tmp[i] += arr2[len(arr2) - 1 - i]

        def add(xs, i, v):
            if i >= len(xs):
                xs.extend([0] * (len(xs) - i + 1))
            xs[i] += v

        # print(tmp)
        i = 0
        while i < len(tmp):
            v = tmp[i]
            tmp[i] = v % 2
            v = v // 2
            if v:
                add(tmp, i + 1, v)
                add(tmp, i + 2, v)
            i += 1

            if (i + 1) == (len(tmp) - 1) and tmp[i] == 2 * (tmp[i + 1]):
                j = i - 1
                while j >= 0 and tmp[j] == 0:
                    j -= 1
                if j == -1:
                    j += 1
                tmp = tmp[:j + 1]
                break

        ans = tmp[::-1]
        return ans


cases = [
    ([1, 1, 1, 1, 1], [1, 0, 1], [1, 0, 0, 0, 0]),
    ([1, 0, 0], [1, 1, 0, 0], [0]),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().addNegabinary, cases)
