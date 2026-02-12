#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        paths.sort(key =lambda x: len(x))

        def get_hash_values(sz, path):
            res = set()
            MOD = 10 ** 15 + 7
            value = 0
            for i in range(sz):
                value = value * n + path[i]
                value = value % MOD

            b = n ** (sz - 1)
            b = b % MOD

            res.add(value)
            for i in range(sz, len(path)):
                value -= b * path[i-sz]
                if value < 0:
                    value += MOD
                value = value * n + path[i]
                value = value % MOD
                res.add(value)

            return res

        def check_overlap(sz):
            set0 = get_hash_values(sz, paths[0])
            for i in range(1, len(paths)):
                set1 = get_hash_values(sz, paths[i])
                set0 = set0 & set1
                if not set0: return False
            return True

        s, e = 1, len(paths[0])
        while s <= e:
            m = (s + e) // 2
            if check_overlap(m):
                s = m + 1
            else:
                e = m - 1
        ans = e
        return ans

if __name__ == '__main__':
    pass
