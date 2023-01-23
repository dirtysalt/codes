#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        ans = 0
        for i in range(len(guess)):
            if guess[i] == answer[i]:
                ans += 1
        return ans

if __name__ == '__main__':
    pass
