#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minOperations(self, n: int) -> int:
        ans = 0
        # x = (n-1)
        # while x >= 0:
        #     ans += x
        #     x -= 2
        # return ans

        if n % 2 == 1:
            ans = (n + 1) * ((n - 3) // 2 + 1) // 2
        else:
            ans = n * ((n - 2) // 2 + 1) // 2
        return ans


import aatest_helper

cases = [
    (3, 2),
    (6, 9),
]

aatest_helper.run_test_cases(Solution().minOperations, cases)
