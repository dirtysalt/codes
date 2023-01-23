#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def toValue(w):
            v = 0
            for c in w:
                v = v * 10 + ord(c) - ord('a')
            return v

        return toValue(firstWord) + toValue(secondWord) == toValue(targetWord)


if __name__ == '__main__':
    pass
