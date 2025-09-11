#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        def norm(x):
            d = {}
            res = []
            for c in x:
                if c not in d:
                    d[c] = len(d)
                res.append(d[c])
            return tuple(res)

        ans = []
        p = norm(pattern)
        for w in words:
            p2 = norm(w)
            if p == p2:
                ans.append(w)
        return ans

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        def norm(x):
            d = [-1] * 26
            sz = 0
            res = 0
            for c in x:
                c2 = ord(c) - ord('a')
                if d[c2] == -1:
                    d[c2] = sz
                    sz += 1
                res = res * 26 + d[c2]
            return res

        ans = []
        p = norm(pattern)
        for w in words:
            p2 = norm(w)
            if p == p2:
                ans.append(w)
        return ans

if __name__ == '__main__':
    pass
