#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        st = []
        a, b = 0, 0

        n = max(len(arr1), len(arr2))
        for i in range(n):
            x = 0
            if i < len(arr1):
                x += arr1[len(arr1) - 1 - i]
            if i < len(arr2):
                x += arr2[len(arr2) - 1 - i]

            a += x
            st.append(a % 2)
            a, b = b + a // 2, a // 2

        while a != 2 * b:
            st.append(a % 2)
            a, b = b + a // 2, a // 2

        while st and st[-1] == 0:
            st.pop()

        if not st:
            return [0]
        ans = st[::-1]
        return ans


cases = [
    ([1, 1, 1, 1, 1], [1, 0, 1], [1, 0, 0, 0, 0]),
    ([1, 0, 0], [1, 1, 0, 0], [0]),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().addNegabinary, cases)
