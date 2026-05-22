#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        def parse(s):
            h, m = s.split(':')
            return int(h) * 60 + int(m)

        start = parse(startTime)
        finish = parse(finishTime)
        if finish < start:
            finish += 24 * 60

        a = (start + 15 - 1) // 15
        b = finish // 15
        ans = b - a
        return ans


if __name__ == '__main__':
    pass
