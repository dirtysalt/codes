#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        from collections import Counter
        cnt = Counter(barcodes)
        import heapq
        hp = []
        for x, c in cnt.items():
            hp.append((-c, x))
        heapq.heapify(hp)

        ans = []
        while hp:
            (c, x) = heapq.heappop(hp)
            c = -c
            if hp:
                (c2, y) = heapq.heappop(hp)
                c2 = -c2
                ans.append(x)
                ans.append(y)
                if c2 > 1:
                    heapq.heappush(hp, (-(c2 - 1), y))

            else:
                ans.append(x)

            if c > 1:
                heapq.heappush(hp, (-(c - 1), x))

        return ans
