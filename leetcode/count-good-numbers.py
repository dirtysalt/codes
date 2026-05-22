#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def countGoodNumbers(self, n: int) -> int:

        MOD = 10 ** 9 + 7
        def pow(x, y):
            res = 1
            while y :
                if y & 0x1:
                    res = res * x
                    res = res % MOD
                x = x * x
                x %=MOD
                y = y >> 1
            return res

        a = pow(5, (n+1)//2)
        b = pow(4, n // 2)

        ans = (a * b) % MOD
        return ans



if __name__ == '__main__':
    pass
