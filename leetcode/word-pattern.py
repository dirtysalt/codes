#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ss = s.split()

        def make_pat(ss):
            res = []
            his = {}
            idx = 0
            for x in ss:
                if x in his:
                    res.append(his[x])
                else:
                    res.append(idx)
                    his[x] = idx
                    idx += 1
            return res

        a = make_pat(ss)
        b = make_pat(pattern)
        ans = a == b
        return ans


cases = [
    ("abba", "dog cat cat dog", True),
    ("abba", "dog dog dog dog", False)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().wordPattern, cases)
