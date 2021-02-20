#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from leetcode import aatest_helper


class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        res, depth = 0, 0
        for c in S:
            if c == '(':
                depth += 1
                continue
            if depth <= 0:
                res += 1
            else:
                depth -= 1

        res += depth
        return res


cases = [
    ("())", 1),
    ("(((", 3),
    ("()", 0),
    ("()))((", 4)
]
sol = Solution()

aatest_helper.run_test_cases(sol.minAddToMakeValid, cases)
