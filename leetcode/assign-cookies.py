#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List

from leetcode import aatest_helper


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i, j, n, m = 0, 0, len(g), len(s)
        res = 0
        while i < n and j < m:
            if s[j] >= g[i]:
                i += 1
                j += 1
                res += 1
            else:
                j += 1
        return res


cases = [
    ([1, 2, 3], [1, 1], 1),
    ([1, 2], [1, 2, 3], 2),
    ([10, 9, 8, 7], [5, 6, 7, 8], 2)
]
sol = Solution()
aatest_helper.run_test_cases(sol.findContentChildren, cases)
