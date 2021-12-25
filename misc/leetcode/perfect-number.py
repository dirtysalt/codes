#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1: return False

        x = 2
        ans = 1
        while x * x < num:
            if num % x == 0:
                y = num // x
                ans += x
                ans += y
                if ans > num:
                    return False
            x += 1

        if x * x == num:
            ans += x
        return ans == num


true, false, null = True, False, None
cases = [
    (28, true),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().checkPerfectNumber, cases)

if __name__ == '__main__':
    pass
