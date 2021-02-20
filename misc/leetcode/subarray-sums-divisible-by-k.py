#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from collections import Counter

from typing import List

from leetcode import aatest_helper


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        rems = Counter()
        res, acc = 0, 0
        rems[0] = 1
        for v in A:
            acc = (acc + v) % K
            res += rems[acc]
            rems[acc] += 1
        return res


cases = [
    ([4, 5, 0, -2, -3, 1], 5, 7),
    ([5, 0], 5, 3),
    ([4, 5, 0], 5, 3)
]
sol = Solution()

aatest_helper.run_test_cases(sol.subarraysDivByK, cases)