#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:

        def doCount(num):
            s = str(num)
            from functools import cache
            @cache
            def f(i, sum, isNum, isLimit):
                if sum > max_sum:
                    return 0

                if i == len(s):
                    return sum >= min_sum and isNum

                res = 0
                down = 0 if isNum else 1
                up = int(s[i]) if isLimit else 9
                for d in range(down, up + 1):
                    res += f(i + 1, sum + d, True, isLimit and d == up)
                return res

            return f(0, 0, True, True)

        a = doCount(num2)
        b = doCount(num1)
        c = (min_sum <= sum(map(int, num1)) <= max_sum)
        ans = (a - b) + c
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ("1", "12", 1, 8, 11),
    ("1", "5", 1, 5, 5),
]

aatest_helper.run_test_cases(Solution().count, cases)

if __name__ == '__main__':
    pass
