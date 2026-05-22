#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        pos = [[] for _ in range(10)]
        for i in reversed(range(len(s))):
            c = ord(s[i]) - ord('0')
            pos[c].append(i)

        for i in range(len(t)):
            c = ord(t[i]) - ord('0')
            if not pos[c]: return False
            p = pos[c][-1]
            pos[c].pop()
            # 确保没有更小的数在这个位置之前
            for j in range(c):
                if not pos[j]: continue
                if pos[j][-1] < p: return False

        return True


cases = [
    ("84532", "34852", True),
    ("34521", "23415", True),
    ("12345", "12435", False),
    ("1", "2", False)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().isTransformable, cases)
