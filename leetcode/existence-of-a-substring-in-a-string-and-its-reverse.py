#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        s2 = ''.join(s[::-1])

        for i in range(0, len(s) - 1):
            if s2.find(s[i:i + 2]) != -1:
                return True

        return False


if __name__ == '__main__':
    pass
