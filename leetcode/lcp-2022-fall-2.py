#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def transportationHub(self, path: List[List[int]]) -> int:
        from collections import Counter
        inc = Counter()
        outc = Counter()
        n = 0
        for a, b in path:
            inc[b] += 1
            outc[a] += 1
            n = max(n, a, b)

        n += 1
        for i in range(n):
            if inc[i] == (n - 1) and outc[i] == 0:
                return i
        return -1


if __name__ == '__main__':
    pass
