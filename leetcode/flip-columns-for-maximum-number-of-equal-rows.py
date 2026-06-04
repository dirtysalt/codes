#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        def flip_pattern(xs):
            fp = []
            for i in range(1, len(xs)):
                fp.append(xs[i] == xs[i - 1])
            return tuple(fp)

        from collections import Counter
        cnt = Counter()
        ans = 0
        for xs in matrix:
            fp = flip_pattern(xs)
            cnt[fp] += 1
            ans = max(ans, cnt[fp])
        return ans
