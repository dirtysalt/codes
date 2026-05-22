#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:

        ans = 0
        for i in range(len(s)):
            v, c = 0, 0
            for j in range(i, len(s)):
                x = s[j]
                if x in 'aeiou':
                    v += 1
                else:
                    c += 1
                if (v == c) and ((v * c) % k == 0):
                    ans += 1
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(s="baeyh", k=2, res=2),
    aatest_helper.OrderedDict(s="abba", k=1, res=3),
    aatest_helper.OrderedDict(s="bcdf", k=1, res=0),
    ("eeebjoxxujuaeoqibd", 8, 4),
]

aatest_helper.run_test_cases(Solution().beautifulSubstrings, cases)

if __name__ == '__main__':
    pass
