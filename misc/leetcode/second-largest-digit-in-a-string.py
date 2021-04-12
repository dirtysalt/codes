#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def secondHighest(self, s: str) -> int:
        cnt = [0] * 10
        for c in s:
            c2 = ord(c) - ord('0')
            if c2 >= 0 and c2 < 10:
                cnt[c2] += 1

        i = 9
        while i >= 0 and cnt[i] == 0: i-=1
        i -= 1
        while i >= 0 and cnt[i] == 0: i-=1;
        if i >= 0: return i
        return -1


if __name__ == '__main__':
    pass
