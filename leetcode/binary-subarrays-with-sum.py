#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        from collections import Counter
        cnt = Counter()
        cnt[0] = 1
        acc = 0
        ans = 0
        for x in A:
            acc += x
            ans += cnt[acc - S]
            cnt[acc] += 1
        return ans
