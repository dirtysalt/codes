#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        n = len(A)
        ss = sum(A)
        if ss % 3 != 0:
            return False

        target = ss//3
        res = 0
        cnt = 0
        for v in A:
            res += v
            if res == target:
                cnt += 1
                res = 0
            else:
                pass
        return cnt >= 3


cases = [
    ([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1], False),
    ([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1], True)
]

import aatest_helper
aatest_helper.run_test_cases(Solution().canThreePartsEqualSum, cases)
