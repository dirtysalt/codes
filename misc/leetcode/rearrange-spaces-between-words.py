#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def reorderSpaces(self, text: str) -> str:
        ss = [x.strip() for x in text.split()]
        blk = 0
        for c in text:
            if c == ' ': blk += 1
        n = len(ss)
        if n == 1:
            avg = 0
        else:
            avg = blk // (n - 1)
        rmd = blk - (n - 1) * avg
        ans = (' ' * avg).join(ss) + ' ' * rmd
        return ans


cases = [
    ("  this   is  a sentence ", "this   is   a   sentence"),
    (" practice   makes   perfect", "practice   makes   perfect "),
    ("hello   world", "hello   world"),
    ("  walks  udp package   into  bar a", "walks  udp  package  into  bar  a "),
    ("a", "a"),
]
import aatest_helper

aatest_helper.run_test_cases(Solution().reorderSpaces, cases)
