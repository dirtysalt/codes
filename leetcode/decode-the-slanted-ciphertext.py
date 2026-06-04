#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols = len(encodedText) // rows

        buf = []
        for c in range(cols):
            r = 0
            for c2 in range(c, cols):
                x = encodedText[r * cols + c2]
                buf.append(x)
                r += 1
                if r >= rows:
                    break

        while buf and buf[-1] == ' ':
            buf.pop()
        ans = ''.join(buf)
        return ans

if __name__ == '__main__':
    pass
