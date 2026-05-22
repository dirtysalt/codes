#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        from collections import Counter, defaultdict
        ans = 0

        def decompose(k):
            # 对k做因子分解，假设包含x ^ c.
            # 如果 v^2 % k == 0的话，那么需要确保
            # v至少整除 x ^ ((c+1)//2)
            # 因为k的范围比较小，所以这里可以直接遍历所有值
            k2 = 1
            for x in range(2, k + 1):
                if k < x: break
                if k % x == 0:
                    c = 0
                    while k % x == 0:
                        k //= x
                        c += 1
                    for _ in range((c + 1) // 2):
                        k2 *= x
            return k2

        v, c = 0, 0
        K2 = decompose(k)
        VC = Counter()
        VC[(0, 0)] += 1
        for i in range(len(s)):
            x = s[i]
            if x in 'aeiou':
                v += 1
            else:
                c += 1
            r = VC[(v - c, v % K2)]
            ans += r
            VC[(v - c, v % K2)] += 1
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
