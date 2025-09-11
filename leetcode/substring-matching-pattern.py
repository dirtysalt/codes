#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        x = p.find('*')
        a, b = p[:x], p[x + 1:]
        pa = s.find(a) if a else 0
        if pa == -1: return False
        pb = s.rfind(b) if b else len(s)
        if pb == -1: return False
        # print(pa, pb)
        if pa + len(a) > pb:
            return False
        return True


true, false, null = True, False, None
import aatest_helper

cases = [
    ("leetcode", "ee*e", true),
    ("leee", "ee*e", true),
    ("car", "c*v", false),
    ("luck", "u*", true),
]

aatest_helper.run_test_cases(Solution().hasMatch, cases)

if __name__ == '__main__':
    pass
