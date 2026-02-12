#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        from collections import defaultdict
        fix = defaultdict(list)
        for x in nums:
            fix[x].append(x)

        for x, y in operations:
            old = fix[x]
            del fix[x]
            fix[y].extend(old)

        rev = {}
        for k, xs in fix.items():
            for x in xs:
                rev[x] = k

        ans = []
        for x in nums:
            ans.append(rev.get(x, x))
        return ans


true, false, null = True, False, None
cases = [
    ([1, 2, 4, 6], [[1, 3], [4, 7], [6, 1]], [3, 2, 7, 1]),
    ([1, 2], [[1, 3], [2, 1], [3, 2]], [2, 1]),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().arrayChange, cases)
