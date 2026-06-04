#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n = len(arr)
        tmp = [(arr[i], i) for i in range(n)]
        tmp.sort()

        ans = [0] * n
        rank = 1
        j = 0
        for i in range(n):
            if tmp[i][0] != tmp[j][0]:
                rank += 1
            ans[tmp[i][1]] = rank
            j = i
        return ans


cases = [
    ([40, 10, 20, 30], [4, 1, 2, 3]),
    ([100, 100, 100], [1, 1, 1]),
    ([], [])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().arrayRankTransform, cases)
