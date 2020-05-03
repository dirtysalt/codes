#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def checkValidString(self, s: str) -> bool:

        dp = {}
        n = len(s)

        def fun(i, d):
            if i == n:
                return d == 0

            key = (i, d)
            if key in dp:
                return dp[key]

            while i < n and s[i] != '*':
                if s[i] == '(':
                    d += 1
                elif s[i] == ')':
                    d -= 1
                if d < 0:
                    break
                i += 1

            if i == n:
                ans = (d == 0)
                dp[key] = ans
                return ans

            if d < 0:
                dp[key] = False
                return False

            assert s[i] == '*'
            ans = False
            if d >= 1:
                ans = ans or fun(i + 1, d - 1)
            ans = ans or fun(i + 1, d)
            ans = ans or fun(i + 1, d + 1)
            dp[key] = ans
            return ans

        ans = fun(0, 0)
        return ans


cases = [
    ("()", True),
    ("(*)", True),
    ("(((*))", True),
    ("((*)))", True),
    ("(*)))", False),
    ("(())((())()()(*)(*()(())())())()()((()())((()))(*", False)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().checkValidString, cases)
