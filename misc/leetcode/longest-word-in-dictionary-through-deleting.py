#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key=lambda x: (-len(x), x))

        def ok(a, b):
            k = 0
            for c in a:
                while k < len(b) and b[k] != c:
                    k += 1
                if k == len(b):
                    return False
                k += 1
            return True

        for a in d:
            if ok(a, s):
                return a
        return ''
