#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def countLargestGroup(self, n: int) -> int:
        from collections import Counter

        sums = Counter()
        max_cnt = 0
        for i in range(1, n + 1):
            x = i
            s = 0
            while x:
                s += x % 10
                x = x // 10
            sums[s] += 1
            max_cnt = max(max_cnt, sums[s])

        ans = 0
        for x, c in sums.items():
            if c == max_cnt:
                ans += 1
        return ans
