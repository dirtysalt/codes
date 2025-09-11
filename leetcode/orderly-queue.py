#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def orderlyQueue(self, S: str, K: int) -> str:
        if K == 1:
            ans = S
            for i in range(len(S)):
                s = S[i:] + S[:i]
                if s < ans:
                    ans = s
        else:
            ans = ''.join(sorted(S))
        return ans


cases = [
    ("cba", 1, "acb"),
    ("baaca", 3, "aaabc"),
    ("xxqjzq", 2, "jqqxxz"),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().orderlyQueue, cases)
