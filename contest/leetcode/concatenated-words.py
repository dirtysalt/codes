#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=lambda x: len(x))
        ws = set()
        ans = []

        def check(i, w):
            for j in range(i + 1, len(w) + 1):
                w1 = w[i:j]
                if w1 in ws and (j == len(w) or check(j, w)):
                    return True

            return False

        for w in words:
            if check(0, w):
                ans.append(w)
            ws.add(w)
        return ans
