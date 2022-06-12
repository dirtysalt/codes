#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        ss = [set() for _ in range(26)]
        for s in ideas:
            c = ord(s[0]) - ord('a')
            tail = s[1:]
            ss[c].add(tail)

        ans = 0
        for i in range(26):
            for j in range(26):
                if i == j: continue
                a = len(ss[i] - ss[j])
                b = len(ss[j] - ss[i])
                ans += a * b
        return ans


true, false, null = True, False, None
cases = [
    (["coffee", "donuts", "time", "toffee"], 6),
    (["lack", "back"], 0),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().distinctNames, cases)

if __name__ == '__main__':
    pass
