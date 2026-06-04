#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        for i in reversed(range(n)):
            if int(num[i]) % 2 == 1:
                return num[:i + 1]
        return ""


if __name__ == '__main__':
    pass
