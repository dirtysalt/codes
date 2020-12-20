#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordsSet = set(words)
        dp = {}

        def search(w):
            if not w:
                return 0

            if w in dp:
                return dp[w]

            ok = -(1 << 30)
            for i in range(1, len(w) + 1):
                w1 = w[:i]
                if w1 in wordsSet:
                    w2 = w[i:]
                    x = search(w2)
                    ok = max(ok, x + 1)
                    if ok >= 2:
                        break
            dp[w] = ok
            return ok

        ans = []
        for w in words:
            cut = search(w)
            if cut >= 2:
                ans.append(w)
        return ans


cases = [
    (["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"],
     ["catsdogcats", "dogcatsdog", "ratcatdogcat"]),
    (["a", "b", "ab", "abc"], ["ab"])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().findAllConcatenatedWordsInADict, cases)
