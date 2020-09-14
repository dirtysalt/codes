#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List

# 可以参考gray-code.py实现
class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        arr = list(range(0, 2 ** n))

        def flip0(arr, s, e):
            if (s + 1) == e:
                return

            m = (s + e) // 2
            flip0(arr, s, m)
            flip0(arr, m + 1, e)
            arr[m + 1:e + 1] = list(reversed(arr[m + 1:e + 1]))
            return

        def flip1(arr, n):
            for i in range(1, n):
                sz = 1 << i
                for j in range(sz, len(arr), 2 * sz):
                    k = j + sz
                    arr[j:k] = list(reversed(arr[j:k]))

        flip0(arr, 0, len(arr) - 1)
        #        flip1(arr, n)
        idx = arr.index(start)
        ans = arr[idx:] + arr[:idx]
        return ans


cases = [
    (3, 2, [2, 6, 7, 5, 4, 0, 1, 3]),
    (2, 3, [3, 2, 0, 1])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().circularPermutation, cases)
