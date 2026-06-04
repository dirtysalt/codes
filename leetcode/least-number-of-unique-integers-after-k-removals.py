#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        from collections import Counter
        cnt = Counter()
        for x in arr:
            cnt[x] += 1
        res = [(k, v) for k, v in cnt.items()]
        res.sort(key=lambda x: x[1])
        n = len(res)
        acc = 0
        ans = 0
        for i in range(n):
            acc += res[i][1]
            if acc > k:
                ans = n - i
                break
        return ans
