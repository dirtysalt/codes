#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)

        from collections import Counter
        c = Counter(arr)
        keys = list(c.keys())
        keys.sort(key = lambda x: c[x], reverse=True)

        res = 0
        ans = 0
        for k in keys:
            res += c[k]
            ans += 1
            if 2 * res >= n:
                break

        return ans
