#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        lo, hi = 0, 0
        if len(s) % 2 != 0: return False
        for i in range(len(s)):
            if locked[i] == '0':
                lo -= 1
                hi += 1
            else:
                if s[i] == '(':
                    hi += 1
                    lo += 1
                else:
                    hi -= 1
                    lo -= 1
            if hi < 0:
                return False
            lo = max(lo, 0)
        return lo <= 0 <= hi


true, false, null = True, False, None
cases = [
    ("))()))", "010100", true),
    ("()()", "0000", true),
    (")", "0", false),
    ("()", "11", true),
    ("())(()(()(())()())(())((())(()())((())))))(((((((())(()))))(",
     "100011110110011011010111100111011101111110000101001101001111", false),
    ("))))(())((()))))((()((((((())())((()))((((())()()))(()", "101100101111110000000101000101001010110001110000000101",
     false),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().canBeValid, cases)

if __name__ == '__main__':
    pass
