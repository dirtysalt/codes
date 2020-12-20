#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List

from leetcode import aatest_helper


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        def make_dist(s):
            v = [0] * 26
            for c in s:
                v[ord(c) - ord('a')] += 1
            return v

        n = len(A)
        if n == 0:
            return []

        inf = 500
        res = [inf] * 26
        for i in range(n):
            tmp = make_dist(A[i])
            for j in range(26):
                res[j] = min(res[j], tmp[j])

        ans = []
        for i in range(26):
            if res[i] and res[i] != inf:
                ans.extend([chr(i + ord('a'))] * res[i])
        return ans


cases = [
    (["bella", "label", "roller"], ["e", "l", "l"]),
    (["cool", "lock", "cook"], ["c", "o"])
]

sol = Solution()
aatest_helper.run_test_cases(sol.commonChars, cases)
