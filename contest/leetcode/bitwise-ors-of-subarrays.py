#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        n = len(A)
        ans, cons = set(), set()
        for i in range(n):
            tmp = set()
            tmp.add(A[i])
            for x in cons:
                tmp.add(x | A[i])
            ans.update(tmp)
            cons = tmp
        return len(ans)


cases = [
    ([1, 2, 4], 6),
    ([1, 1, 2], 3),
    ([4, 1, 15], 4)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().subarrayBitwiseORs, cases)
