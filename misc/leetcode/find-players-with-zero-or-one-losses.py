#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        from collections import Counter
        c = Counter()
        m = set()

        for w, l in matches:
            m.add(w)
            m.add(l)
            c[l] += 1

        ans = [[], []]
        for x in sorted(m):
            v = c[x]
            if v in (0, 1):
                ans[v].append(x)
        return ans


if __name__ == '__main__':
    pass
