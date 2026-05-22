#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        idx = set()
        for w in words:
            for sz in range(1, len(w)):
                for i in range(len(w) - sz + 1):
                    s = w[i:i + sz]
                    idx.add(s)

        ans = []
        for w in words:
            if w in idx:
                ans.append(w)
        return ans
