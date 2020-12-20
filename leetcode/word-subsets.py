#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        from collections import Counter
        bc = Counter()
        for x in B:
            tc = Counter()
            for c in x:
                tc[c] += 1
            for c in tc:
                bc[c] = max(bc[c], tc[c])

        ans = []
        for x in A:
            tc = Counter()
            for c in x:
                tc[c] += 1
            ok = True
            for c in bc:
                if tc[c] < bc[c]:
                    ok = False
                    break
            if ok:
                ans.append(x)
        return ans
