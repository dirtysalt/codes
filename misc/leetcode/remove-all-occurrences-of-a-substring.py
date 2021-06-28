#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:

        while len(s) >= len(part):
            idx = s.find(part)
            if idx == -1: break
            s = s[:idx] + s[idx + len(part):]

        return s


if __name__ == '__main__':
    pass
