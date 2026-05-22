#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minimizeResult(self, expression: str) -> str:
        a, b = expression.split('+')
        ans = 1 << 63
        xx = ''

        def ev(s, a, b, c, d):
            a = int(a) if a else 1
            d = int(d) if d else 1
            bc = int(b) + int(c)
            # print(s, a, bc, d)
            return a * bc * d

        for i in range(len(a)):
            for j in range(len(b)):
                s = a[:i] + '(' + a[i:] + '+' + b[:j + 1] + ')' + b[j + 1:]
                res = ev(s, a[:i], a[i:], b[:j + 1], b[j + 1:])
                if res < ans:
                    ans = res
                    xx = s
        return xx


true, false, null = True, False, None
cases = [
    ("247+38", "2(47+38)"),
    ("12+34", "1(2+3)4"),
    ("999+999", "(999+999)")
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minimizeResult, cases)

if __name__ == '__main__':
    pass
