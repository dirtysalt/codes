#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        bc = set(brokenLetters)

        ans = 0
        for w in text.split():
            ok = True
            for c in w:
                if c in bc:
                    ok = False
                    break
            if ok: ans += 1

        return ans


if __name__ == '__main__':
    pass
