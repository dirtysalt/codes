#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            tmp = 0
            while num:
                tmp += num % 10
                num = num // 10
            num = tmp
        return num


# abc = 100 * a + 10 * b + c -> a + b + c
# offset = 99 * a + 9 * b = 9(11*a+b)
class Solution2:
    def addDigits(self, num: int) -> int:
        if num == 0: return 0
        ans = num % 9
        if ans == 0:
            ans = 9
        return ans


cases = [
    (38, 2)
]
import aatest_helper

aatest_helper.run_test_cases(Solution().addDigits, cases)
