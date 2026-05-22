#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        tmp = [0] * (n + 1)
        for i in range(n):
            tmp[i] = tmp[i - 1] ^ arr[i]

        ans = []
        for a, b in queries:
            c = tmp[a - 1] ^ tmp[b]
            ans.append(c)
        return ans


cases = [
    ([1, 3, 4, 8], [[0, 1], [1, 2], [0, 3], [3, 3]], [2, 7, 14, 8]),
    ([4, 8, 2, 10], [[2, 3], [1, 3], [0, 0], [0, 3]], [8, 0, 4, 4]),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().xorQueries, cases)
