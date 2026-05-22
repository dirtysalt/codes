#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def nearestPalindromic(self, n: str) -> str:

        def fun(i, j):
            if i > j:
                return ['']

            has_ending = True
            if i == j:
                has_ending = False

            a = int(n[i])
            sub = fun(i + 1, j - 1)
            res = [n[i] + x + (n[i] if has_ending else '') for x in sub]
            if (a - 1) >= 0:
                c = str(a - 1)
                res.append(c + '9' * max(0, (j - i - 1)) + (c if has_ending else ''))
            if (a + 1) <= 9:
                c = str(a + 1)
                res.append(c + '0' * max(0, (j - i - 1)) + (c if has_ending else ''))

            return res

        opts = fun(0, len(n) - 1)
        if len(n) > 1:
            opts.append('9' * (len(n) - 1))
        opts.append('1' + '0' * (len(n) - 1) + '1')
        # print(opts)

        ans = []
        ogn = int(n)
        for x in opts:
            if x == n:
                continue
            ans.append(int(x))
        ans.sort(key=lambda x: (abs(x - ogn), x))
        return str(ans[0])


cases = [
    ('123', '121'),
    ('99', '101'),
    ('1', '0')
]

import aatest_helper

aatest_helper.run_test_cases(Solution().nearestPalindromic, cases)
