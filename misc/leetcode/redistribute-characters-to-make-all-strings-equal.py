#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        cnt = [0] * 26
        n = len(words)

        for w in words:
            for c in w:
                c2 = ord(c) - ord('a')
                cnt[c2] += 1

        for x in cnt:
            if x % n != 0:
                return False
        return True


if __name__ == '__main__':
    pass
