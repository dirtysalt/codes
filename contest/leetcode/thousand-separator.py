#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n == 0:
            return '0'

        p = 1
        tmp = []
        while n:
            x = n % 10
            n = n // 10
            tmp.append(chr(x + ord('0')))
            if p % 3 == 0 and n != 0:
                tmp.append('.')
            p += 1
        ans = ''.join(reversed(tmp))
        return ans


cases = [
    (1234, "1.234"),
    (123456789, "123.456.789"),
    (0, '0')
]
import aatest_helper

aatest_helper.run_test_cases(Solution().thousandSeparator, cases)
