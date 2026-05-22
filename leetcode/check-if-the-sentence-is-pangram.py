#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        cnt = [0] * 26
        for c in sentence:
            ci = ord(c) - ord('a')
            cnt[ci] += 1

        for i in range(26):
            if cnt[i] == 0:
                return False
        return True

if __name__ == '__main__':
    pass
