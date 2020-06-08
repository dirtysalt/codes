#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr = arr.copy()
        n = len(arr)
        arr.sort()
        m = arr[(n - 1) // 2]
        arr.sort(key=lambda x: (abs(x - m), x), reverse=True)
        ans = arr[:k]
        return ans


cases = [
    ([6, 7, 11, 7, 6, 8], 5, [11, 8, 6, 6, 7]),
    ([-7, 22, 17, 3], 2, [22, 17]),
    ([6, -3, 7, 2, 11], 3, [-3, 11, 2]),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().getStrongest, cases)
