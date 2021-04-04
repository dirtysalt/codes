#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        x, y = coordinates
        a = ord(x) - ord('a')
        b = ord(y) - ord('0') - 1
        return (a + b) % 2 == 1

if __name__ == '__main__':
    pass
