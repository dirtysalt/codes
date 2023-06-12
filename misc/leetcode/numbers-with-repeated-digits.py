#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        s = str(n)

        from functools import cache
        @cache
        def f(i, mask, isNum, isLimit):
            if i == len(s):
                return isNum

            res = 0
            if not isNum:
                res += f(i + 1, mask, False, False)

            down = 0 if isNum else 1
            up = int(s[i]) if isLimit else 9
            for d in range(down, up + 1):
                if not (mask & (1 << d)):
                    res += f(i + 1, mask | (1 << d), True, isLimit and d == up)
            return res

        a = f(0, 0, False, True)
        ans = n - a
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    (20, 1),
    (100, 10),
    (1000, 262),
]

aatest_helper.run_test_cases(Solution().numDupDigitsAtMostN, cases)

if __name__ == '__main__':
    pass
