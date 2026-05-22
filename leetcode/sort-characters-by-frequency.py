#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        cnt = Counter()
        for c in s:
            cnt[c] += 1

        ans = ''
        for c, t in cnt.most_common():
            ans = ans + c * t
        return ans
