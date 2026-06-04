#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        vis = set()
        j = 0
        ans = 0
        for i in range(len(s)):
            c = s[i]
            if c in vis:
                while j <= i and s[j] != c:
                    vis.remove(s[j])
                    j += 1
                vis.remove(c)
                j += 1
            else:
                ans = max(ans, (i - j + 1))
            vis.add(c)
        return ans


cases = [
    ('c', 1),
    (' ', 1),
    ('abcabcbb', 3)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().lengthOfLongestSubstring, cases)
