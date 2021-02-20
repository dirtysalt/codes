#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key=lambda x: -len(x))

        d = {}
        index = []
        for idx, w in enumerate(words):
            if w in d:
                continue
            for i in range(len(w) - 1):
                s = w[i:]
                d[s] = idx
            index.append(idx)

        ans = len(index)  # '#'
        for idx in index:
            ans += len(words[idx])
        return ans


cases = [
    (["time", "me", "bell"], 10)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minimumLengthEncoding, cases)
