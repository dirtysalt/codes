#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def splitString(self, s: str) -> bool:

        import functools

        @functools.lru_cache(maxsize=None)
        def test(last, i):
            if i == len(s): return True
            now = 0
            for j in range(i, len(s)):
                now = now * 10 + int(s[j])
                if (now + 1) == last and test(now, j + 1):
                    return True
            return False

        last = 0
        for i in range(len(s) - 1):
            last = last * 10 + int(s[i])
            if test(last, i + 1):
                return True
        return False

if __name__ == '__main__':
    pass
