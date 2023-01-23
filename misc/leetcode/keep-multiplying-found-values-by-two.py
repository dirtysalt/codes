#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        xs = set(nums)
        while True:
            if original not in xs:
                break
            original *= 2
        return original


if __name__ == '__main__':
    pass
