#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left = [0] * 26
        right = [0] * 26
        for i in range(len(s)):
            c = ord(s[i]) - ord('a')
            right[c] = i
        for i in reversed(range(len(s))):
            c = ord(s[i]) - ord('a')
            left[c] = i

        ans = 0
        for c in range(26):
            l, r = left[c], right[c]
            mark = [0] * 26
            for i in range(l + 1, r):
                mark[ord(s[i]) - ord('a')] = 1
            ans += sum(mark)
        return ans


if __name__ == '__main__':
    pass
