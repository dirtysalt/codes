#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def lastSubstring(self, s: str) -> str:
        n = len(s)
        max_len = 0
        choices = list(range(n))

        while len(choices) > 1:
            max_len += 1
            max_value = max((s[i] for i in choices if i < n))
            min_value = min((s[i] for i in choices if i < n))
            choices = [i+1 for i in choices if i < n and s[i] == max_value]

            if max_value == min_value:
                choices = choices[:1]

        p = choices[0]
        return s[p-max_len:]


import aatest_helper

cases = [
    ("abab", "bab"),
    ("leetcode", 'tcode'),
    ("cacacb", "cb"),    
]

aatest_helper.run_test_cases(Solution().lastSubstring, cases)
