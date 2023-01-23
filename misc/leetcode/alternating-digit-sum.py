#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        ans = 0
        f = 1
        while n >= 10:
            ans += f * (n % 10)
            n = n // 10
            f = -f

        ans += f * n
        if f == -1:
            ans = -ans
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    (521, 4),
    (111, 1),
    (886996, 0),
]

aatest_helper.run_test_cases(Solution().alternateDigitSum, cases)

if __name__ == '__main__':
    pass
