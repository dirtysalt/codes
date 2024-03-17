#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        n = len([x for x in s if x == c])
        return n * (n + 1) // 2


if __name__ == '__main__':
    pass
