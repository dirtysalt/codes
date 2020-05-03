#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        map = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}

        st = 0
        pos = {st: -1}
        ans = 0

        for i, c in enumerate(s):
            if c in map:
                v = map[c]
                # print(st, v, st ^ (1 << v))
                st ^= (1 << v)

            if st in pos:
                j = pos[st]
                ans = max(ans, i - j)
            else:
                pos[st] = i
        return ans


cases = [
    ("eleetminicoworoep", 13),
    ("leetcodeisgreat", 5),
    ("bcbcbc", 6)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().findTheLongestSubstring, cases)
