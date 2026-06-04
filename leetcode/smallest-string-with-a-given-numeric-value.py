#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = []
        for i in range(n):
            j = (n - i - 1)
            x = max(1, k - 26 * j)
            k -= x
            ans.append(x)

        ans = ''.join([chr(x + ord('a') - 1) for x in ans])
        return ans


cases = [
    (3, 27, "aay"),
    (5, 73, "aaszz")
]

import aatest_helper

aatest_helper.run_test_cases(Solution().getSmallestString, cases)
