#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from collections import Counter


class Solution:
    def maxFreqSum(self, s: str) -> int:
        cnt1 = Counter()
        cnt2 = Counter()
        for c in s:
            if c in 'aeiou':
                cnt1[c] += 1
            else:
                cnt2[c] += 1
        return max(cnt1.values() or [0]) + max(cnt2.values() or [0])


if __name__ == '__main__':
    pass
