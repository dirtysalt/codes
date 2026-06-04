#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        import functools
        @functools.lru_cache(maxsize=None)
        def query(i, j):
            if i == len(word1): return -1
            if j == len(word2): return 1
            if word1[i] < word2[j]: return -1
            if word1[i] > word2[j]: return 1
            return query(i + 1, j + 1)

        i, j = 0, 0
        ans = ''
        while i < len(word1) and j < len(word2):
            c1 = word1[i]
            c2 = word2[j]
            if query(i, j) == 1:
                ans += c1
                i += 1
            else:
                ans += c2
                j += 1

        ans += word1[i:]
        ans += word2[j:]
        return ans


cases = [
    ("cabaa", "bcaaa", "cbcabaaaaa"),
    ("abcabc", "abdcaba", "abdcabcabcaba"),
    ("guguuuuuuuuuuuuuuguguuuuguug", "gguggggggguuggguugggggg", "guguuuuuuuuuuuuuuguguuuuguugguggggggguuggguuggggggg"),
    ("uuurruuuruuuuuuuuruuuuu", "urrrurrrrrrrruurrrurrrurrrrruu",
     "uuuurruuuruuuuuuuuruuuuurrrurrrrrrrruurrrurrrurrrrruu"),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().largestMerge, cases)
