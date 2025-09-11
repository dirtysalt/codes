#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        acc = sum(chalk)
        k = k % acc

        t = 0
        for i in range(len(chalk)):
            c = chalk[i]
            t += c
            if k < t:
                return i
        return 0


if __name__ == '__main__':
    pass
