#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def find(bars):
            maxsz = 1
            bars.sort()
            i = 0
            while i < len(bars):
                j = i + 1
                while j < len(bars) and bars[j] - bars[j - 1] == 1:
                    j += 1
                sz = j + 1 - i
                maxsz = max(maxsz, sz)
                i = j
            return maxsz

        h = find(hBars)
        v = find(vBars)
        # print(h, v)
        return min(h, v) ** 2


if __name__ == '__main__':
    pass
