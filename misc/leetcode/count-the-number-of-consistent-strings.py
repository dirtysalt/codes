#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        cs = set(allowed)

        def isAllow(word):
            for c in word:
                if c not in cs:
                    return False
            return True

        ans = 0
        for w in words:
            if isAllow(w):
                ans += 1

        return ans
