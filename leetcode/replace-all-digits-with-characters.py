#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def replaceDigits(self, s: str) -> str:
        ans = []
        i = 0
        while (i+1) < len(s):
            c = s[i]
            c2 = chr(ord(c) + int(s[i+1]))
            ans.append(c)
            ans.append(c2)
            i += 2
        if i < len(s):
            ans.append(s[i])
        return ''.join(ans)


if __name__ == '__main__':
    pass
