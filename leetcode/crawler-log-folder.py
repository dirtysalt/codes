#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for x in logs:
            if x == './':
                continue
            elif x == '../':
                ans -= 1
                ans = max(ans, 0)
            else:
                ans += 1
        return ans


cases = [
    (["d1/", "d2/", "../", "d21/", "./"], 2),
    (["d1/", "d2/", "./", "d3/", "../", "d31/"], 3),
    (["d1/", "../", "../", "../"], 0)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minOperations, cases)
