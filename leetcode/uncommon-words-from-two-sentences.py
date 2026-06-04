#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        from collections import Counter
        cntA = Counter()
        cntB = Counter()
        for s in A.split():
            cntA[s] += 1
        for s in B.split():
            cntB[s] += 1

        ans = []
        ans += [s for s in cntA if cntA[s] == 1 and cntB[s] == 0]
        ans += [s for s in cntB if cntB[s] == 1 and cntA[s] == 0]
        return ans
